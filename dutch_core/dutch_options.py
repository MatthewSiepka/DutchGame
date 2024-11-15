from dataclasses import dataclass
from dutch_core.card.card import CardsRank, CardsColor

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
    CardsRank.KING: {
        CardsColor.CLUBS: 13,
        CardsColor.HEARTS: 0,
        CardsColor.SPADES: 13,
        CardsColor.DIAMONDS: 0,
    }
}


@dataclass
class DutchOptions:
    card_values: dict
    cards_on_start: int
    cards_to_check: int


DEFAULT_OPTIONS = DutchOptions(DEFAULT_CARD_VALUES, 4, 2)
