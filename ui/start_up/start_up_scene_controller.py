import curses

from ui.scene.scene_controller import SceneController
from ui.start_up.start_up_scene_model import StartUpSceneModel


class StartUpSceneController(SceneController):
    model: StartUpSceneModel

    def __init__(self, model: StartUpSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def key_input(self, key):
        if (
                key == ord(" ") or
                (ord("0") <= key <= ord("9")) or
                (ord("a") <= key <= ord("z")) or
                (ord("A") <= key <= ord("a"))
        ):
            self.model.name += chr(key)

        if key == 127 and len(self.model.name) > 0:
            self.model.name = self.model.name[:-1]

        if key == 10:
            if len(self.model.name) > 0:
                self.change_scene_function("mode_selector", self.model.name)
