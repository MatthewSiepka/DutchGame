from dutch_core.card import Card, CardsColor, CardsRank, create_card_deck

deck = create_card_deck()
print(deck)
print(deck[0])

card = Card(CardsColor.CLUBS, CardsRank.ACE)
print(card.card_color)

print(card.card_value)