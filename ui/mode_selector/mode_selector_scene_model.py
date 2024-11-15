from ui.scene.scene_model import SceneModel


class ModeSelectorSceneModel(SceneModel):
    name: str
    active: int
    error: str

    def __init__(self):
        self.name = ""
        self.active = 0
        self.error = ""

    def get_name(self):
        return self.name

    def update_name(self, name: str):
        self.name = name