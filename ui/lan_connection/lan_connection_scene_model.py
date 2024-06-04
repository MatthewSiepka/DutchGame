from ui.scene.scene_model import SceneModel


class LanConnectionSceneModel(SceneModel):
    name: str
    host: str
    port: str
    active: int
    error: str

    def __init__(self):
        self.name = ""
        self.host = ""
        self.port = ""
        self.active = 0
        self.error = ""

    def get_name(self):
        return self.name

    def update_name(self, name: str):
        self.name = name