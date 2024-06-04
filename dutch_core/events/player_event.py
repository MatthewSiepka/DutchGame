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
    player: str | None
    move: PlayerMove
    details: None | DetailsCardId | DetailsOtherPlayerCard | DetailsForRearranging


def details_to_dict(details: None | DetailsCardId | DetailsOtherPlayerCard | DetailsForRearranging):
    if details is None:
        return None
    data = {}
    if isinstance(details, DetailsCardId):
        data = {
            "type": "detailsCardId",
            "card": details.card
        }
    elif isinstance(details, DetailsOtherPlayerCard):
        data = {
            "type": "detailsOtherPlayerCard",
            "card": details.card,
            "player": details.player
        }
    elif isinstance(details, DetailsForRearranging):
        data = {
            "type": "detailsForRearranging",
            "playerOne": details.player_one,
            "playerTwo": details.player_two,
            "playerOneCard": details.player_one_card,
            "playerTwoCard": details.player_two_card
        }
    return data


def player_event_to_dict(player_event: PlayerEvent):
    data = {
        "type": "PlayerEvent",
        "player": player_event.player,
        "move": player_event.move.value,
        "details": details_to_dict(player_event.details)
    }
    return data


def dict_to_details(details: dict):
    if details is None:
        return None
    if details["type"] == "detailsCardId":
        return DetailsCardId(details["card"])
    if details["type"] == "detailsOtherPlayerCard":
        return DetailsOtherPlayerCard(details["card"], details["player"])
    if details["type"] == "DetailsForRearranging":
        return DetailsForRearranging(
            details["playerOne"],
            details["playerTwo"],
            details["playerOneCard"],
            details["playerTwoCard"]
        )


def dict_to_player_event(player_event: dict):
    event = PlayerEvent(
        player_event["player"],
        PlayerMove(player_event["move"]),
        dict_to_details(player_event["details"])
    )
    return event
