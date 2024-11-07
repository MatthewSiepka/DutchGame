import curses

from ui.scene.scene import Scene
from ui.waiting_room.waiting_room_scene_controller import WaitingRoomSceneController
from ui.waiting_room.waiting_room_scene_model import WaitingRoomSceneModel
from ui.waiting_room.waiting_room_scene_view import WaitingRoomSceneView


class WaitingRoomScene(Scene):
    scene_model: WaitingRoomSceneModel

    def __init__(self, stdscr: curses.window):
        super().__init__(stdscr)
        self.scene_model = WaitingRoomSceneModel()
        self.scene_controller = WaitingRoomSceneController(self.scene_model)
        self.scene_view = WaitingRoomSceneView(stdscr, self.scene_model)
        self.name = "waiting_room"

    def change_scene_listener(self, args):
        self.scene_model.player_interface = args[0]
        if isinstance(self.scene_controller, WaitingRoomSceneController):
            self.scene_model.player_interface.init_start_game_event(self.scene_controller.start_game_event)
        if len(args) > 1:
            self.scene_model.game_interface = args[1]
