from ui.scene.scene_model import SceneModel


class StartUpSceneModel(SceneModel):
    name: str

    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name

    def update_name(self, name: str):
        self.name = name