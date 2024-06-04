import curses

from ui.gui_utility.add_center_text import add_center_text
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
from ui.scene.scene_view import SceneView


class LanConnectionSceneView(SceneView):
    model: LanConnectionSceneModel

    def __init__(self, stdscr: curses.window, model: LanConnectionSceneModel):
        super().__init__(stdscr)
        self.model = model

    def is_active(self, mode_id: int):
        return curses.color_pair(2) if self.model.active == mode_id else curses.color_pair(3)
    def render(self):
        height, width = self.stdscr.getmaxyx()
        self.stdscr.addstr(0, 0, self.model.error, curses.color_pair(4))
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr, "Insert Host:", height // 2 - 4, self.is_active(0))
        add_center_text(self.stdscr, self.model.host, height // 2 - 2, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr, "Insert Port:", height // 2, self.is_active(1))
        add_center_text(self.stdscr, self.model.port, height // 2 + 2, curses.A_BOLD | curses.COLOR_WHITE)

