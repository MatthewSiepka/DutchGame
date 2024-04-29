from dataclasses import dataclass
from dutch_core.player_move import PlayerMove


# Details for Player Event:
@dataclass
class DetailsCardId:
    card: int


@dataclass
class DetailsOtherPlayerCard:
    card: int
    player: str


@dataclass
class DetailsForRearranging:
    player_one: str
    player_two: str
    player_one_card: int
    player_two_card: int


@dataclass
class PlayerEvent:
    player: str
    move: PlayerMove
    details: None | DetailsCardId | DetailsOtherPlayerCard | DetailsOtherPlayerCard | DetailsForRearranging