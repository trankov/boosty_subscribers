import eel
from conf.const import CURR_PORT, EXT_ALLOWED, GUI_PATH, SCREEN


def run():
    eel.init(
        path=GUI_PATH,
        allowed_extensions=EXT_ALLOWED,
        js_result_timeout=4000,
    )
    eel.start(
        "main.html",
        port=CURR_PORT,
        mode="custom",
        cmdline_args=[
            "/Applications/Yandex.app/Contents/MacOS/Yandex",
            f"--app=http://localhost:{CURR_PORT}/main.html",
            "--new-window",
        ],
        # jinja_templates=JINJA_TMPL,
        size=(SCREEN.width // 4, SCREEN.height // 1.1),
        position=(SCREEN.width // 6, SCREEN.height // 11),
    )
