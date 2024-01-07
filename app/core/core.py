import csv
from dataclasses import dataclass, field
from datetime import date
from io import StringIO, TextIOWrapper


@dataclass
class Subscriber:
    """
    Подписчик со всей информацией. Принимает строку из CSV в виде словаря
    и преобразует типы, если необходимо.

    Свойства после инициализации:
    ```
        name: str
        email: str
        type: str
        price: float
        total_money: float
        start_date: date
        end_date: date | None
        level_name: str
        active: bool
    ```

    Свойство `active` возвращает `True` если подписка активна (время окончания
    отсутствует, цена не равна 0).
    """

    name: str
    email: str
    type: str  # {'following', 'subscription'}
    price: str | float
    total_money: str | float  # '928,14'
    start_date: str | date  # '2023-07-10',
    end_date: str | date | None  # '-',
    level_name: str

    def __post_init__(self):
        if isinstance(self.start_date, str):
            self.start_date = date.fromisoformat(self.start_date)
        if isinstance(self.end_date, str):
            self.end_date = (
                date.fromisoformat(self.end_date) if self.end_date != "-" else None
            )
        if isinstance(self.price, str):
            self.price = float(self.price.replace(",", "."))
        if isinstance(self.total_money, str):
            self.total_money = float(self.total_money.replace(",", "."))

    @property
    def active(self):
        """
        Определяет активность подписчика по цене подписки и дате окончания
        """
        assert isinstance(self.price, float)
        return self.end_date is None and self.price > 0


@dataclass
class SubscriberList:
    """
    Информация о подписчиках. Принимает список `subscribers` и формирует
    список `active_subscribers`, а также список цен на подписку (`prices`).
    Эти значения доступны в качестве атрибутов после инициализации.

    Методы:
    - `select_price(price): list[Subscriber]`: выбирает подписчиков по цене
    - `group_prices(price): dict[float, list[Subscriber]]`: группирует
       подписчиков по ценам
    - `report(sort_desc=False): None`: выводит список подписчиков, сортируя
       его согласно параметру `sort_desc`.
    """

    subscribers: list[Subscriber]

    active_subscribers: list[Subscriber] = field(init=False)
    prices: tuple = field(init=False)

    def __post_init__(self):
        self.active_subscribers = [sub for sub in self.subscribers if sub.active]
        self.prices = tuple(sorted(self._collect_prices()))

    def _collect_prices(self) -> set[float]:
        """
        Формирует список цен на подписку
        """
        return {
            sub.price for sub in self.active_subscribers if isinstance(sub.price, float)
        }

    def select_price(self, price: float) -> list[Subscriber]:
        """
        Выбирает подписчиков по указанной цене подписки
        """
        return (
            [
                sub
                for sub in reversed(
                    sorted(self.active_subscribers, key=lambda sub: sub.total_money)
                )
                if sub.price == price
            ]
            if price in self.prices
            else []
        )

    def group_prices(self, price: float) -> dict[float, list[Subscriber]]:
        """
        Группирует подписчиков по ценам на подписку в словарь, где ключ
        цена подписки, а значение - список подписчиков.
        """
        return {price: self.select_price(price)} if price in self.prices else {}

    def report_text(self, sort_desc=False) -> str:
        """
        Создаёт список подписчиков, сортируя его согласно параметру `sort_desc`.
        """
        report_text = ""
        for price in reversed(self.prices) if sort_desc else self.prices:
            headline = f"Подписчики за {price} руб.:"
            hr = "—" * len(headline)
            report_text += "\n".join((hr, headline, hr))
            report_text += "\n"
            pricelist = self.select_price(price)
            report_text += "\n".join(sub.name for sub in pricelist)
            report_text += "\n"
        return report_text

    def report_html(self, sort_desc=False) -> str:
        """
        Создаёт HTML-список подписчиков, сортируя его согласно параметру `sort_desc`.
        """
        html = ""
        for price in reversed(self.prices) if sort_desc else self.prices:
            html += f'<h2 class="subscriber-price">Подписчики за {price} руб.</h2>'
            html += "<div class='subscriber-name'>"
            html += '</div><div class="subscriber-name">'.join(
                sub.name for sub in self.select_price(price)
            )
            html += "</div>"
        return html

    def report(self, sort_desc=False) -> None:
        """
        Выводит список подписчиков, сортируя его согласно параметру `sort_desc`.
        """
        print(self.report_text(sort_desc))


class CSVManager:
    """
    Выполняет загрузку из CSV. Формирует `SubscriberList` и помещает его
    в атрибут `table`.
    """

    csv_stream: TextIOWrapper
    table: SubscriberList

    def __init__(self, filename) -> None:
        self._init_csv_stream_from_file(filename)
        self.table = self._get_csv_table_from_stream(self.csv_stream)

    def _init_csv_stream_from_file(self, path: str) -> None:
        self.csv_stream = open(path, "r", encoding="utf-8-sig")

    def __del__(self):
        self.__close_csv_stream()

    def __close_csv_stream(self) -> None:
        if self.csv_stream and not self.csv_stream.closed:
            self.csv_stream.close()

    def _get_api_responce(self) -> None:
        """
        Получает сырой CSV из API Boosty
        """
        return None

    def _get_io_stream(self, content: bytes) -> StringIO:
        """
        Предполагается передавать requests.Response.content
        """
        return StringIO(content.decode("utf-8-sig"))

    def _get_csv_table_from_stream(
        self, csv_stream: StringIO | TextIOWrapper
    ) -> SubscriberList:
        """
        Превращает CSV stream в список со словарями в таблице
        """
        with csv_stream as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";", quotechar='"')
            return SubscriberList([Subscriber(**row) for row in reader])


# if __name__ == "__main__":
#     stat: SubscriberList = CSVManager().table
#     stat.report()
