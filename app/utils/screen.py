from typing import NamedTuple

from AppKit import NSScreen


class Resolution(NamedTuple):
    x: int
    y: int
    width: int
    height: int


def screen_resolutions():
    screens = NSScreen.screens()
    screen = screens[0]  # First screen is always the main screen
    frame = screen.frame
    if callable(frame):
        frame = frame()
    return Resolution(
        x=int(frame.origin.x),
        y=int(frame.origin.y),
        width=int(frame.size.width),
        height=int(frame.size.height),
    )

if __name__ == '__main__':
    print(screen_resolutions())
