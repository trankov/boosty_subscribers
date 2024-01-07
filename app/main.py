import eel
from core import html_report
from launch import run
from utils.dialogs import file_open_dialog


class EventManager:
    sender: str
    event: str

    def __init__(self, sender, event):
        self.sender = sender
        self.event = event

    def resolve(self):
        self.spinner(True)
        method_name = f"{self.sender}_{self.event}"
        getattr(self, method_name)()
        self.spinner(False)

    def btnFile_click(self):
        if filename := file_open_dialog():
            report = html_report(filename, True)
            self.caption("Список подписчиков из файла:")
            eel.change_content("lblResult", report)
        else:
            self.caption("Получить список донатеров")

    def btnFetch_click(self):
        report = html_report(sort_desc=True)
        self.caption("Список подписчиков из интернета:")
        eel.change_content("lblResult", report)

    def caption(self, text, style=""):
        eel.change_content("lblHeader", text)
        if style:
            eel.change_style("lblHeader", style)

    def spinner(self, show=True):
        display = "block" if show else "none"
        eel.change_style("spinnerFetch", f"display: {display};")


@eel.expose
def resolve_event(sender, event):
    manager = EventManager(sender, event)
    manager.resolve()


run()
