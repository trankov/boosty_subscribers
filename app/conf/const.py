from pathlib import Path

from utils.launch import random_port
from utils.screen import Resolution, screen_resolutions
from utils.launch import read_allowed_extensions

BASE_PATH: Path = Path(__file__).parent.parent.resolve()
GUI_PATH: str = str(BASE_PATH / "gui")
# JINJA_TMPL: str = str(BASE_PATH / "gui" / "templates")
SCREEN: Resolution = screen_resolutions()
CURR_PORT: int = random_port()
EXT_ALLOWED: list[str] = read_allowed_extensions()
