from dutch_core.card.card import Card, dict_to_card
from dataclasses import dataclass
from dutch_core.events.player_info import PlayerInfo
from dutch_core.player_move import PlayerMove


@dataclass
class Board:
    card_on_used_stack: Card
    players: list[PlayerInfo]
    player_cards: int
    player_turn: str | None
    moves_possible: list[PlayerMove]


def dict_to_board(data: dict):
    if data is None:
        return None
    card_on_used_stack = dict_to_card(data["cardOnUsedStack"])
    players = [PlayerInfo(p["player"], p["cards"]) for p in data["players"]]
    player_cards = data["playerCards"]
    player_turn = data["playerTurn"]
    move_possible = [PlayerMove(move) for move in data["moves_possible"]]
    return Board(card_on_used_stack, players, player_cards, player_turn, move_possible)


def board_to_json(board: Board):
    if board is None:
        return None
    data = {
        "cardOnUsedStack": board.card_on_used_stack.to_dict(),
        "players": [{"player": player_info.player, "cards": player_info.cards} for player_info in board.players],
        "playerCards": board.player_cards,
        "playerTurn": board.player_turn,
        "moves_possible": [player_move.value for player_move in board.moves_possible]
    }
    return data
