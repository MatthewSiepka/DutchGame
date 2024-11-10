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
        self.model.name_input.input_key(key)

        if key == 10:
            if len(self.model.get_name()) > 0:
                self.change_scene_function("mode_selector", self.model.get_name())
