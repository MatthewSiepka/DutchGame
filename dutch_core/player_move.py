from enum import Enum, auto

class PlayerMove(Enum):
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
    PUT_CARD_ON_USED_STACK = auto()  # when one card was taken from stack or used stack
