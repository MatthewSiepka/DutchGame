import curses

from ui.lan_connection.lan_connection_scene_controller import LanConnectionSceneController
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
from ui.lan_connection.lan_connection_scene_view import LanConnectionSceneView
from ui.scene.scene import Scene


class LanConnectionScene(Scene):
    scene_model: LanConnectionSceneModel

    def __init__(self, stdscr: curses.window):
        super().__init__(stdscr)
        self.scene_model = LanConnectionSceneModel()
        self.scene_controller = LanConnectionSceneController(self.scene_model)
        self.scene_view = LanConnectionSceneView(stdscr, self.scene_model)
        self.name = "lan_connection"

    def change_scene_listener(self, args):
        self.scene_model.name = args[0]