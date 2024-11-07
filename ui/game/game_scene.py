import curses

from ui.game.game_scene_controller import GameSceneController
from ui.game.game_scene_model import GameSceneModel
from ui.game.game_scene_view import GameSceneView
from ui.scene.scene import Scene


class GameScene(Scene):
    scene_model: GameSceneModel

    def __init__(self, stdscr: curses.window):
        super().__init__(stdscr)
        self.scene_model = GameSceneModel()
        self.scene_controller = GameSceneController(self.scene_model)
        self.scene_view = GameSceneView(stdscr, self.scene_model)
        self.name = "game"

    def change_scene_listener(self, args):
        self.scene_model.player_interface = args[0]