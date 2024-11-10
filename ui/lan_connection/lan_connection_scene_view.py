import curses

from ui.gui_utility.Input.input import Input, AcceptableCharacters
from ui.gui_utility.add_center_text import add_center_text
from ui.gui_utility.color_scheme import curses_colors
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
from ui.scene.scene_view import SceneView


class LanConnectionSceneView(SceneView):
    model: LanConnectionSceneModel

    def __init__(self, stdscr: curses.window, model: LanConnectionSceneModel):
        super().__init__(stdscr)
        self.model = model
        self.model.host_input = Input(stdscr, AcceptableCharacters.ALL)
        self.model.port_input = Input(stdscr, AcceptableCharacters.NUMBERS)
        self.model.host_input.set_active(True)

    def is_active(self, mode_id: int):
        return curses.A_BOLD | curses_colors["magenta_black"] if self.model.active == mode_id else curses_colors["white_black"]


    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, "Connect to game host:", height // 2 - 6, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, "Insert Host:", height // 2 - 4, self.is_active(0))
        self.model.host_input.render(height // 2 - 2)
        add_center_text(self.stdscr, "Insert Port:", height // 2, self.is_active(1))
        self.model.port_input.render(height // 2 + 2)
        add_center_text(self.stdscr, self.model.error,height // 2 + 6, curses.A_BOLD | curses_colors["red_black"])
        add_center_text(self.stdscr, "Move between inputs using arrow keys (up and down)", height // 2 + 8, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, "Press \"Enter\" to Connect", height // 2 + 10, curses.A_BOLD | curses_colors["white_black"])


