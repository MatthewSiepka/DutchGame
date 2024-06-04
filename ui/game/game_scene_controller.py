import curses
import socket

from dutch.lan_player_interface import LanPlayerInterface
from ui.game.game_scene_model import GameSceneModel
from ui.scene.scene_controller import SceneController


class GameSceneController(SceneController):
    model: GameSceneModel

    def __init__(self, model: GameSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def key_input(self, key):
        ...
        # self.change_scene_function("mode_selector", self.model.name)

