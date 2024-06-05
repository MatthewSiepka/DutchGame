from enum import Enum, auto

from dutch.player_interface import PlayerInterface
from ui.scene.scene_model import SceneModel


class GameSelectionType(Enum):
    ACTIONS = auto()
    PLAYER_CARDS = auto()
    ALL_CARDS = auto()
    ALL_CARDS_SELECTION = auto()


class GameSceneModel(SceneModel):
    player_interface: PlayerInterface | None
    game_selection: GameSelectionType
    actions_selected: int | None
    player_cards_selected: int | None
    player_selected: int | None
    all_cards_selected: list[int] | None

    def __init__(self):
        self.player_interface = None
        self.actions_selected = 0
        self.player_cards_selected = 0
        self.all_cards_selected = None
        self.player_selected = 0
        self.game_selection = GameSelectionType.ACTIONS
