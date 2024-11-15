import curses

from ui.gui_utility.Input.input import Input, AcceptableCharacters
from ui.gui_utility.add_center_text import add_center_text
from ui.gui_utility.color_scheme import curses_colors
from ui.scene.scene_view import SceneView
from ui.start_up.start_up_scene_model import StartUpSceneModel


class StartUpSceneView(SceneView):
    model: StartUpSceneModel

    def __init__(self, stdscr: curses.window, model: StartUpSceneModel):
        super().__init__(stdscr)
        self.model = model
        self.model.name_input = Input(stdscr, AcceptableCharacters.ALL)
        self.model.name_input.set_active(True)


    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, "Insert your Name:", height // 2 - 4, curses.A_BOLD | curses_colors["white_black"])
        self.model.name_input.render(height // 2 - 2)
        add_center_text(self.stdscr, self.model.error_message, height // 2, curses.A_BOLD | curses_colors["red_black"])
        add_center_text(self.stdscr, "Press \"ENTER\" to Continue", height // 2 + 2, curses.A_BOLD | curses_colors["white_black"])
