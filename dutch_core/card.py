import random
from enum import Enum, auto


class CardsColor(Enum):
    CLUBS = {
        "name": "clubs",
        "color": "black",
        "icon": "♣︎"
    }
    DIAMONDS = {
        "name": "diamonds",
        "color": "red",
        "icon": "♦︎"
    }
    HEARTS = {
        "name": "hearts",
        "color": "red",
        "icon": "♥︎"
    }
    SPADES = {
        "name": "spades",
        "color": "black",
        "icon": "♠︎"
    }


# CARD_COLORS = [CardsColor.CLUBS, CardsColor.SPADES, ]


class CardsRank(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


# Cards Values Can Be Set for All cards Colors by setting it to int or separate for each Color eg.:
# CardsRank.ACE: 1,
# or
# CardsRank.ACE: {
#   CardColor.Clubs: 1,
#   CardColor.Hearts: 2,
#   CardColor.Diamonds: 3,
#   CardColor.Spades: 4,
# }


DEFAULT_CARD_VALUES = {
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
    CardsRank.KING: 13
}


class Card:
    card_rank = None
    card_color = None
    card_value = None
    card_value_sheet = None

    def __init__(self, card_color: CardsColor, card_rank: CardsRank, card_value_sheet: {} = None):
        if card_value_sheet is None:
            card_value_sheet = DEFAULT_CARD_VALUES
        self.card_color = card_color
        self.card_rank = card_rank
        self.card_value_sheet = card_value_sheet
        self.init_card_value()

    def init_card_value(self):
        values_for_card = self.card_value_sheet[self.card_rank]
        if isinstance(values_for_card, dict):
            self.card_value = values_for_card[self.card_color]
        elif isinstance(values_for_card, int):
            self.card_value = values_for_card
        else:
            raise TypeError("card value can be only value for every card (int) or value for seperate cards {"
                            "CardsColor.sparde: 1, ...} ")

    def __str__(self):
        return str(self.card_color.value['icon']) + " " + self.card_rank.value + ", card value:" + str(self.card_value)


def create_card_deck(card_value_sheet: dict | None = None) -> list[Card]:
    deck = []
    for color in CardsColor:
        for rank in CardsRank:
            deck.append(Card(color, rank, card_value_sheet))
    return deck


def shuffle_cards(cards: list[Card]):
    random.shuffle(cards)
