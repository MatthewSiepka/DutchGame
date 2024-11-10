from ui.gui_utility.Input.input import Input
from ui.scene.scene_model import SceneModel


class StartUpSceneModel(SceneModel):
    name_input: Input
    error_message: str

    def __init__(self):
        self.error_message = ""

    def get_name(self):
        return self.name_input.text

