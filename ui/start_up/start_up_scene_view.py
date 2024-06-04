import curses

from dutch_core.card.card import Card, CardsColor, CardsRank
from ui.gui_utility.add_center_text import add_center_text
from ui.scene.scene_view import SceneView
from ui.start_up.start_up_scene_model import StartUpSceneModel


class StartUpSceneView(SceneView):
    model: StartUpSceneModel

    def __init__(self, stdscr: curses.window, model: StartUpSceneModel):
        super().__init__(stdscr)
        self.model = model

    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr, "Insert your Name:", height // 2 - 4, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr, self.model.name, height // 2 - 2, curses.A_BOLD | curses.COLOR_WHITE)