from enum import Enum, auto


class GameChange(Enum):
    CARDS_DEALT = "card_dealt"
    END_OF_GAME = "end_of_game"
