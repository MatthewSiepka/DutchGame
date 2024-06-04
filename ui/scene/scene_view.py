import curses
from abc import abstractmethod, ABC

from ui.scene.scene_model import SceneModel


class SceneView(ABC):
    stdscr: curses.window
    CYAN_COLOR: int
    MAGENTA_COLOR: int
    WHITE_COLOR: int

    def __init__(self, stdscr: curses.window):
        self.stdscr = stdscr
        self.CYAN_COLOR = curses.color_pair(1)
        self.MAGENTA_COLOR = curses.color_pair(1)
        self.WHITE_COLOR = curses.color_pair(1)


    @abstractmethod
    def render(self):
        ...
