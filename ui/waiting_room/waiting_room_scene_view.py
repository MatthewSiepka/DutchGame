import curses

from ui.gui_utility.add_center_text import add_center_text
from ui.scene.scene_view import SceneView
from ui.start_up.start_up_scene_model import StartUpSceneModel
from ui.waiting_room.waiting_room_scene_model import WaitingRoomSceneModel


class WaitingRoomSceneView(SceneView):
    model: WaitingRoomSceneModel

    def __init__(self, stdscr: curses.window, model: WaitingRoomSceneModel):
        super().__init__(stdscr)
        self.model = model

    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", height // 2 - 10, curses.A_BOLD | curses.COLOR_WHITE)
        if self.model.game_interface is not None and self.model.game_interface.server is not None:
            add_center_text(
                self.stdscr,
                f"Waiting on port: {self.model.game_interface.server.port}",
                height // 2 - 10,
                curses.A_BOLD | curses.COLOR_WHITE
            )
            if len(self.model.player_interface.players) > 1:
                add_center_text(
                    self.stdscr,
                    "Start Game",
                    height // 2 - (-len(self.model.player_interface.players) * 2), curses.color_pair(2))

        add_center_text(
            self.stdscr,
            "Players in lobby:",
            height // 2 - 4,
            curses.A_BOLD | curses.COLOR_WHITE
        )
        for i, player in enumerate(self.model.player_interface.players):
            add_center_text(
                self.stdscr,
                player,
                (height // 2) - ((-i * 2) + 2),
                curses.A_BOLD | curses.COLOR_WHITE
            )