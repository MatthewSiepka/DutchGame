from dutch_core.card import CardsRank, CardsColor, shuffle_cards, create_card_deck, Card

"""
player_data = [
    {
        "name": "test1",
    },
    {
        "name": "test2",
    },
    {
        "name": "test3",
    }, 
]
"""


class DutchGameData:
    stack: list[Card] | None = None
    used_stack: list[Card] | None = None
    players_cards: dict | None = None

    def __init__(self, options: dict, players_data: list[dict]):
        self.init_card_stacks(options)
        self.init_players_decks(players_data)

    def init_card_stacks(self, options: dict):
        self.used_stack = []
        self.stack = create_card_deck(options)
        shuffle_cards(self.stack)

    def init_players_decks(self, players_data: list[dict]):
        self.players_cards = {player["name"]: [] for player in players_data}

    def take_card_from_stack(self) -> Card:
        return self.stack.pop()

    def take_card_from_used_stack(self) -> Card:
        return self.used_stack.pop()

    def put_card_on_used_stack(self, card: Card):
        self.used_stack.append(card)

    def check_players_card(self, player_name: str, card_index: int):
        return self.players_cards[player_name][card_index]

    def replace_players_card(self, player_name: str, card: Card, card_index: int) -> Card:
        temp = self.players_cards[player_name][card_index]
        self.players_cards[player_name][card_index] = card
        return temp

    def rearrange_players_cards(self, player_one: str, player_one_card_index: int, player_two: str, player_two_card_index: int):
        player_one_deck = self.players_cards[player_one]
        player_two_deck = self.players_cards[player_two]
        temp = player_one_deck[player_one_card_index]
        player_one_deck[player_one_card_index] = player_two_deck[player_two_card_index]
        player_two_deck[player_two_card_index] = temp

    def add_player_card(self, player_name: str, card: Card):
        self.players_cards[player_name].append(card)

    def print_game_data(self):
        print(self.players_cards)
        for player_name in self.players_cards:
            print("Player:", player_name, "cards:")
            for card in self.players_cards[player_name]:
                print(card, sep="; ")
