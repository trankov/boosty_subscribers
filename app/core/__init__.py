from .core import CSVManager


def html_report(filename=None, sort_desc=False) -> str:
    manager = CSVManager(filename)
    stat = manager.table
    return stat.report_html(sort_desc)


def text_report(filename=None, sort_desc=False) -> str:
    manager = CSVManager(filename)
    stat = manager.table
    return stat.report_text(sort_desc)
