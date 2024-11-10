import curses
from abc import abstractmethod, ABC



class SceneView(ABC):
    stdscr: curses.window

    def __init__(self, stdscr: curses.window):
        self.stdscr = stdscr


    @abstractmethod
    def render(self):
        ...
