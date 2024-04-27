from enum import Enum, auto
from card import CardsRank, CardsColor

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
}
}


class user_moves(Enum):
    LOOK_AT_OWN_CARDS = auto()  # at start
    LOOK_AT_ANY_CARDS = auto()  # if card was putted on used stack, card was from deck, and the card was Queen
    CHANGE_PLACE_OF_CARDS = auto()  # if card was putted on used stack, card was from deck, and the card was Jack

    DUTCH = auto()  # at start of players turn

    JUMP_IN = auto()  # allways

    TAKE_CARD_FROM_STACK = auto()  # when it is players turn and no other move was performed on this move with
    # exception for dutch or jump in
    TAKE_CARD_FROM_USED_STACK = auto()  # when it is players turn and no other move was performed on this move with
    # exception for dutch or jump in

    REPLACE_CARD_FROM_OWN_DECK = auto()  # when one card was taken from stack or used stack
    PUT_CAR_ON_STACK = auto()  # when one card was taken from stack or used stack


user_possible_moves = {
    "start": [
        {
            "user_move": None,
            "moves_possible": [user_moves.LOOK_AT_OWN_CARDS, user_moves.JUMP_IN],
        }
    ],
    "user_turn": [
        {
            "user_move": 0,
            "moves_possible": [
                user_moves.DUTCH,
                user_moves.TAKE_CARD_FROM_STACK,
                user_moves.TAKE_CARD_FROM_USED_STACK,
                user_moves.JUMP_IN
            ]
        },
        {
            "user_move": 1,
            "moves_possible": [
                user_moves.PUT_CAR_ON_STACK,
                user_moves.REPLACE_CARD_FROM_OWN_DECK
            ]
        }
    ]
}

event = {
    "player": 0,
    "move": user_moves.REPLACE_CARD_FROM_OWN_DECK,
    "details": {
        "card": 1,
    },
    "new_card_on_used_stack": "a"
}


class DutchGame:
    players = None
    player_turn = None

