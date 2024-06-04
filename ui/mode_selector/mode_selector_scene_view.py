import curses
from curses.textpad import rectangle

from ui.gui_utility.add_center_text import add_center_text
from ui.mode_selector.mode_selector_scene_model import ModeSelectorSceneModel
from ui.scene.scene_view import SceneView


class ModeSelectorSceneView(SceneView):
    model: ModeSelectorSceneModel

    def __init__(self, stdscr: curses.window, model: ModeSelectorSceneModel):
        super().__init__(stdscr)
        self.model = model

    def is_active(self, mode_id: int):
        return curses.color_pair(2) if self.model.active == mode_id else curses.color_pair(3)

    def render(self):

        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr, f"Hello {self.model.name}!", height // 2 - 8, curses.A_BOLD | curses.COLOR_WHITE)
        rectangle(self.stdscr, height // 2 - 6, width // 2 - 20, height // 2 + 6, width // 2 + 20)
        add_center_text(self.stdscr, f"Chose game mode", height // 2 - 6, self.WHITE_COLOR)
        add_center_text(self.stdscr, "Host Lan Game", height // 2 - 2, self.is_active(0))
        add_center_text(self.stdscr, "Join Lan Game", height // 2, self.is_active(1))
        add_center_text(self.stdscr, "Play Vs AI", height // 2 + 2, self.is_active(2))
