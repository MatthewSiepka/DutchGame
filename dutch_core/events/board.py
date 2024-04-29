from dutch_core.card.card import Card
from dataclasses import dataclass
from dutch_core.events.player_info import PlayerInfo
from dutch_core.player_move import PlayerMove


@dataclass
class Board:
    card_on_used_stack: Card
    players: list[PlayerInfo]
    player_cards: int
    player_turn: str
    moves_possible: list[PlayerMove]
