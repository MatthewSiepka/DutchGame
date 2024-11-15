import curses

from ui.mode_selector.mode_selector_scene_controller import ModeSelectorSceneController
from ui.mode_selector.mode_selector_scene_model import ModeSelectorSceneModel
from ui.mode_selector.mode_selector_scene_view import ModeSelectorSceneView
from ui.scene.scene import Scene


class ModeSelectorScene(Scene):
    scene_model: ModeSelectorSceneModel

    def __init__(self, stdscr: curses.window):
        super().__init__(stdscr)
        self.scene_model = ModeSelectorSceneModel()
        self.scene_controller = ModeSelectorSceneController(self.scene_model)
        self.scene_view = ModeSelectorSceneView(stdscr, self.scene_model)
        self.name = "mode_selector"

    def change_scene_listener(self, args):
       self.scene_model.name = args[0]

