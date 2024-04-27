from dutch_core.card import Card, CardsColor, CardsRank, create_card_deck
from dutch_core.dutch_game_data import DutchGameData
from dutch_core.dutch_game import get_default_options

players = [
    {
        "name": "test1",
        "id": 0
    },
    {
        "name": "test2",
        "id": 1
    }
]

print(CardsColor['SPADES'])

game_data = DutchGameData(get_default_options()["card_values"], players)


for i in range(4):
    for player in players:
        game_data.add_player_card(player["name"], game_data.take_card_from_stack())

game_data.print_game_data()
