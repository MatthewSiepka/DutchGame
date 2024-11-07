import curses

from ui.scene.scene_controller import SceneController
from ui.waiting_room.waiting_room_scene_model import WaitingRoomSceneModel


class WaitingRoomSceneController(SceneController):
    model: WaitingRoomSceneModel

    def __init__(self, model: WaitingRoomSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def start_game_event(self):
        self.change_scene_function("game", self.model.player_interface)

    def key_input(self, key):
        if key == 10:
            if len(self.model.player_interface.players) > 1 and self.model.game_interface is not None:
                self.model.game_interface.start_lan_game()
