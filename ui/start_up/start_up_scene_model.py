from ui.gui_utility.Input.input import Input
from ui.scene.scene_model import SceneModel


class StartUpSceneModel(SceneModel):
    name_input: Input

    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name_input.text

    def update_name(self, name: str):
        self.name = name
