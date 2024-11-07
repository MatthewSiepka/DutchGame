from dutch.game_interface import GameInterface
from dutch.player_interface import PlayerInterface
from ui.scene.scene_model import SceneModel


class WaitingRoomSceneModel(SceneModel):
    name: str
    player_interface: PlayerInterface | None
    game_interface: GameInterface | None

    def __init__(self):
        self.name = ""
        self.player_interface = None
        self.game_interface = None

    def get_name(self):
        return self.name

    def update_name(self, name: str):
        self.name = name