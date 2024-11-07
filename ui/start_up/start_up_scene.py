import curses

from ui.scene.scene import Scene
from ui.start_up.start_up_scene_controller import StartUpSceneController
from ui.start_up.start_up_scene_model import StartUpSceneModel
from ui.start_up.start_up_scene_view import StartUpSceneView


class StartUpScene(Scene):
    scene_model: StartUpSceneModel

    def __init__(self, stdscr: curses.window):
        super().__init__(stdscr)
        self.scene_model = StartUpSceneModel()
        self.scene_controller = StartUpSceneController(self.scene_model)
        self.scene_view = StartUpSceneView(stdscr, self.scene_model)
        self.name = "start_up"

    def change_scene_listener(self, args):
        ...