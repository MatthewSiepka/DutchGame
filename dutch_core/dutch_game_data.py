from dutch_core.card import CardsRank, CardsColor, shuffle_cards, create_card_deck

"""
player_data = [
    {
        "name": "test1",
        "id": 0,
    },
    {
        "name": "test2",
        "id": 0,
    },
    {
        "name": "test3",
        "id": 0,
    }, 
    



"""


class DutchGameData:
    stack = None
    used_stack = None
    players_cards = None

    def __init__(self, options, players_data):
        self.init_card_stacks(options)
        self.init_players_decks(players_data)

    def init_card_stacks(self, options):
        self.used_stack = []
        self.stack = create_card_deck(options)
        shuffle_cards(self.stack)

    def init_players_decks(self, players_data):
        self.players_cards = {player["name"]: [] for player in players_data}

    def take_card_from_stack(self):
        return self.stack.pop()

    def take_card_from_used_stack(self):
        return self.used_stack.pop()

    def put_card_on_used_stack(self, card):
        self.used_stack.append(card)

    def check_players_card(self, player_name, card_index):
        return self.players_cards[player_name][card_index]

    def replace_players_card(self, player_name, card, card_index):
        temp = self.players_cards[player_name][card_index]
        self.players_cards[player_name][card_index] = card
        return temp

    def rearrange_players_cards(self, player_one, player_one_card_index, player_two, player_two_card_index):
        player_one_deck = self.players_cards[player_one]
        player_two_deck = self.players_cards[player_two]
        temp = player_one_deck[player_one_card_index]
        player_one_deck[player_one_card_index] = player_two_deck[player_two_card_index]
        player_two_deck[player_two_card_index] = temp

    def add_player_card(self, player_name, card):
        self.players_cards[player_name].append(card)

    def print_game_data(self):
        print(self.players_cards)
        for player_name in self.players_cards:
            print("Player:", player_name, "cards:")
            for card in self.players_cards[player_name]:
                print(card, sep="; ")
