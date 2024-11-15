from enum import Enum, auto


class PlayerMove(Enum):
    LOOK_AT_OWN_CARDS = "lookAtOwnCards"  # at start
    LOOK_AT_ANY_CARDS = "lookAtAnyCards"  # if card was putted on used stack, card was from deck, and the card was Queen
    REARRANGE_PLACE_OF_CARDS = "rearrangePlaceOfCards"  # if card was putted on used stack, card was from deck, and the card was Jack

    DUTCH = "dutch"  # at start of players turn

    JUMP_IN = "jumpIn"  # allways

    TAKE_CARD_FROM_STACK = "takeCardFromStack"  # when it is players turn and no other move was performed on this move with
    # exception for dutch_old or jump in
    TAKE_CARD_FROM_USED_STACK = "takeCardFromUsedStack"  # when it is players turn and no other move was performed on this move with
    # exception for dutch_old or jump in

    REPLACE_CARD_FROM_OWN_DECK = "replaceCardFromOwnDeck"  # when one card was taken from stack or used stack
    PUT_CARD_ON_USED_STACK = "putCardOnUsedStack"  # when one card was taken from stack or used stack


def player_move_to_text(player_move: PlayerMove):
    match player_move:
        case PlayerMove.LOOK_AT_OWN_CARDS:
            return "Look At Your Card"
        case PlayerMove.LOOK_AT_ANY_CARDS:
            return "Look At Card"
        case PlayerMove.REARRANGE_PLACE_OF_CARDS:
            return "Rearrange Place Of Two Cards"
        case PlayerMove.DUTCH:
            return "Dutch"
        case PlayerMove.JUMP_IN:
            return "Jump In"
        case PlayerMove.TAKE_CARD_FROM_STACK:
            return "Take Card From Stack"
        case PlayerMove.TAKE_CARD_FROM_USED_STACK:
            return "Take Card From Used Stack"
        case PlayerMove.REPLACE_CARD_FROM_OWN_DECK:
            return "Replace Card From Your Deck"
        case PlayerMove.PUT_CARD_ON_USED_STACK:
            return "Put Card On Used Stack"
