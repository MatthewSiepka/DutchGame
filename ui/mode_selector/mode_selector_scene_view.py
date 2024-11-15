import curses
from curses.textpad import rectangle

from ui.gui_utility.add_center_text import add_center_text
from ui.gui_utility.color_scheme import curses_colors
from ui.mode_selector.mode_selector_scene_model import ModeSelectorSceneModel
from ui.scene.scene_view import SceneView


class ModeSelectorSceneView(SceneView):
    model: ModeSelectorSceneModel

    def __init__(self, stdscr: curses.window, model: ModeSelectorSceneModel):
        super().__init__(stdscr)
        self.model = model

    def is_active(self, mode_id: int):
        return curses.A_BOLD | curses_colors["magenta_black"] if self.model.active == mode_id else curses_colors["white_black"]

    def render(self):

        height, width = self.stdscr.getmaxyx()
        center_height = height // 2

        add_center_text(self.stdscr, "Dutch Game", center_height - 10, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, f"Hello {self.model.name}!",center_height - 8, curses.A_BOLD | curses_colors["white_black"])
        rectangle(self.stdscr, height // 2 - 6, width // 2 - 20,center_height + 6, width // 2 + 20)
        add_center_text(self.stdscr, f"Chose game_old mode", center_height - 6, curses_colors["cyan_black"])
        add_center_text(self.stdscr, "Host Lan Game", center_height - 2, self.is_active(0))
        add_center_text(self.stdscr, "Join Lan Game", center_height, self.is_active(1))
        # add_center_text(self.stdscr, "Play Vs AI", height // 2 + 2, self.is_active(2))
        add_center_text(self.stdscr, "Navigate using arrow keys (up down)", center_height + 8, curses.A_BOLD | curses_colors["white_black"])
        add_center_text(self.stdscr, "Press \"ENTER\" to Continue", center_height + 10, curses.A_BOLD | curses_colors["white_black"])

