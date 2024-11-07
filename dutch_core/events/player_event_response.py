import json

from dutch_core.events.player_info import PlayerInfo
from dutch_core.events.status import Status
from dutch_core.events.player_event import PlayerEvent, DetailsCardId, DetailsOtherPlayerCard, DetailsForRearranging, \
    player_event_to_dict, dict_to_player_event
from dataclasses import dataclass
from dutch_core.card.card import Card, CardsRank, CardsColor, dict_to_card
from dutch_core.events.board import Board, board_to_json, dict_to_board
from dutch_core.game_change import GameChange
from dutch_core.player_move import PlayerMove


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


def translate_player_event_response_to_json(event: PlayerEventResponse):
    data = {
        "event": "GameEvent",
        "status": event.status.value,
        "gameChange": None if event.game_change is None else event.game_change.value,
        "playerEvent": player_event_to_dict(event.player_event),
        "detailsForPlayer": None if event.details_for_player is None else event.details_for_player.to_dict(),
        "changeOnBoard": board_to_json(event.change_on_board),
        "jumpInDetails": None if event.jump_in_details is None else event.jump_in_details.to_dict(),
        "playerWon": event.player_won,
        "message": event.message
    }
    return data


def translate_dict_to_player_event_response(event: dict):
    if not event["event"] == "GameEvent":
        return None
    status = None if event["status"] is None else Status(event["status"])
    game_change = None if event["gameChange"] is None else GameChange(event["gameChange"])
    player_event = dict_to_player_event(event["playerEvent"])
    details_for_player = dict_to_card(event["detailsForPlayer"])
    change_on_board = dict_to_board(event["changeOnBoard"])
    jump_in_details = dict_to_card(event["jumpInDetails"])
    player_won = event["playerWon"]
    message = event["message"]
    return PlayerEventResponse(
        status,
        game_change,
        player_event,
        details_for_player,
        change_on_board,
        jump_in_details,
        player_won,
        message
    )


a = PlayerEventResponse(
    Status.SUCCESS,
    GameChange.CARDS_DEALT,
    PlayerEvent("test", PlayerMove.LOOK_AT_OWN_CARDS, None),
    None,
    Board(
        Card(CardsColor.CLUBS, CardsRank.JACK),
        [PlayerInfo("test", 1)],
        1,
        "test",
        [PlayerMove.LOOK_AT_OWN_CARDS]
    ),
    None,
    None,
    "test"
)
