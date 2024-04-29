from dutch_core.events.status import Status
from dutch_core.events.player_event import PlayerEvent
from dataclasses import dataclass
from dutch_core.card.card import Card
from dutch_core.events.board import Board
from dutch_core.game_change import GameChange


@dataclass
class PlayerEventResponse:
    status: Status
    game_change: GameChange | None
    player_event: PlayerEvent
    details_for_player: None | Card
    change_on_board: Board | None
    jump_in_details: None | Card
    player_won: None | str
    message: None | str
