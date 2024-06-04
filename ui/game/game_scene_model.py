from dutch.player_interface import PlayerInterface
from ui.scene.scene_model import SceneModel


class GameSceneModel(SceneModel):
    player_interface: PlayerInterface | None

    def __init__(self):
        player_interface = None
