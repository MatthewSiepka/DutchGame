from enum import Enum, auto
from dutch_core.card import CardsRank, CardsColor, Card
from dutch_core.dutch_game_data import DutchGameData
from dataclasses import dataclass

DEFAULT_OPTIONS = {
    "card_values": {
        CardsRank.ACE: 1,
        CardsRank.TWO: 2,
        CardsRank.THREE: 3,
        CardsRank.FOUR: 4,
        CardsRank.FIVE: 5,
        CardsRank.SIX: 6,
        CardsRank.SEVEN: 7,
        CardsRank.EIGHT: 8,
        CardsRank.NINE: 9,
        CardsRank.TEN: 10,
        CardsRank.JACK: 11,
        CardsRank.QUEEN: 12,
        CardsRank.KING: {
            CardsColor.CLUBS: 13,
            CardsColor.HEARTS: 0,
            CardsColor.SPADES: 13,
            CardsColor.DIAMONDS: 0,
        },
    },
    "cards_on_start": 4,
    "cards_to_check": 2
}


def get_default_options():
    return DEFAULT_OPTIONS.copy()


class UserMoves(Enum):
    LOOK_AT_OWN_CARDS = auto()  # at start
    LOOK_AT_ANY_CARDS = auto()  # if card was putted on used stack, card was from deck, and the card was Queen
    REARRANGE_PLACE_OF_CARDS = auto()  # if card was putted on used stack, card was from deck, and the card was Jack

    DUTCH = auto()  # at start of players turn

    JUMP_IN = auto()  # allways

    TAKE_CARD_FROM_STACK = auto()  # when it is players turn and no other move was performed on this move with
    # exception for dutch or jump in
    TAKE_CARD_FROM_USED_STACK = auto()  # when it is players turn and no other move was performed on this move with
    # exception for dutch or jump in

    REPLACE_CARD_FROM_OWN_DECK = auto()  # when one card was taken from stack or used stack
    PUT_CARD_ON_STACK = auto()  # when one card was taken from stack or used stack


@dataclass
class MoveDetails:
    card = None  # player or player one card
    player_one_name = None  # player one name (for ranging)
    player_two_name = None  # player two name (for ranging)
    player_two_card = None  # player two card (for ranging)


@dataclass
class Move:
    player_name: str
    move: UserMoves
    details: MoveDetails


@dataclass
class Event:
    legal: bool
    move: Move
    player_moves: list[UserMoves]
    details_for_player: Card | None


class IllegalMove(Exception):
    def __init__(self, user_name, message):
        super("Move performed by " + user_name + " is illegal, move: " + message)


"""
player
    name
    cards_checked
    possible_moves
    event_listener: lambda(event)
"""

"""
move
    player_name: str
    move: UserMoves
    details: Details
"""

"""
event
    legal: bool 
    move: Move
    user_possible_moves: [Move]
    details_for_player: Card/None
"""


class Player:
    name = None
    possible_moves = None
    event_listener = None

    def __init__(self, name, event_listener):
        self.name = name
        self.event_listener = event_listener


class DutchGame:
    players = None
    players_order = None
    player_turn = None
    dutch = None
    options = None
    game_data = None
    game_ended = False
    card_selected = None

    def __init__(self, options=None):
        if options is None:
            options = DEFAULT_OPTIONS
        self.options = options
        self.players_order = []
        self.players = {}

    def add_player(self, name, user_event_listener):
        new_player = Player(name, user_event_listener)
        self.players_order.append(new_player)
        self.players[name] = new_player

    def init_game(self):
        players_list = []
        for player in self.players_order:
            players_list.append({"name": player.name})
            player.cards_checked = 0

        self.game_data = DutchGameData(self.options["card_values"], players_list)

    def remove_player_possible_move(self, player_name: str, move: Move):
        self.players[player_name].possible_moves.remove(move)

    def looking_faze(self):
        for player in self.players_order:
            player.possible_moves = []
            for _ in range(self.options["cards_to_check"]):
                player.possible_moves.append(UserMoves.LOOK_AT_OWN_CARDS)

    def playing_faze(self):
        self.next_player_turn()
        self.set_not_players_turn()

    def set_not_players_turn(self):
        for player in self.players_order:
            player.possible_moves = [UserMoves.JUMP_IN]

    def set_next_player_turn(self):
        self.set_not_players_turn()
        self.players_order[self.player_turn] = [
            UserMoves.TAKE_CARD_FROM_STACK,
            UserMoves.TAKE_CARD_FROM_USED_STACK,
        ]

    def next_player_turn(self):
        if self.player_turn is None or self.player_turn == len(self.players_order) - 1:
            self.player_turn = 0
        else:
            self.player_turn += 1
        return not (self.dutch is not None and self.dutch == self.player_turn)

    def inform_players(self, move: Move, details: Card | None, legal=True):
        event_for_player = Event(legal, move, self.players[move.player_name].possible_moves, details)

        if not legal:
            self.players[move.player_name].event_listener(event_for_player)
            return

        for player in self.players:
            if player.name == move.player_name:
                player.event_listener(event_for_player)
            else:
                event = Event(legal, move, player.possible_moves, None)
                player.event_listener(event)

    def look_at_own_cards(self, move: Move):
        card = self.game_data.check_players_card(move.player_name, move.details)
        self.inform_players(move, card)
        self.remove_player_possible_move(self, move.player_name, move.move)

    def look_at_any_cards(self, move: Move):
        ...

    def rearrange_place_of_cards(self, move: Move):
        ...

    def perform_move(self, move: Move):
        match move.move:
            case UserMoves.LOOK_AT_OWN_CARDS:
                self.look_at_own_cards(move)
            case UserMoves.LOOK_AT_ANY_CARDS:
                ...
            case UserMoves.REARRANGE_PLACE_OF_CARDS:
                ...
            case UserMoves.DUTCH:
                ...
            case UserMoves.JUMP_IN:
                ...
            case UserMoves.TAKE_CARD_FROM_STACK:
                ...
            case UserMoves.TAKE_CARD_FROM_USED_STACK:
                ...
            case UserMoves.REPLACE_CARD_FROM_OWN_DECK:
                ...
            case UserMoves.REPLACE_CARD_FROM_OWN_DECK:
                ...
            case UserMoves.PUT_CARD_ON_STACK:
                ...

    def user_move(self, move: Move):
        player_name = move.player_name
        try:
            if move.move not in self.players[player_name].possible_moves:
                raise IllegalMove(move.player_name, "player can't perform this move")
            self.perform_move(move)
        except IllegalMove:
            self.inform_players(move, None, False)
