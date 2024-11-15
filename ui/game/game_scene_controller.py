import curses

from dutch_core.player_move import PlayerMove
from ui.game.game_scene_model import GameSceneModel, GameSelectionType
from ui.scene.scene_controller import SceneController


class GameSceneController(SceneController):
    model: GameSceneModel

    def __init__(self, model: GameSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def action_handler(self):
        board = self.model.player_interface.last_game_event.change_on_board


    def key_input(self, key):
        board = self.model.player_interface.last_game_event.change_on_board
