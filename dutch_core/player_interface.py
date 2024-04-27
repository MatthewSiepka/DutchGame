
class PlayerInterface:
    name = None
    player_possible_moves = []
    dutch_game = None
    card_deck = None

    def __init__(self, name, dutch_game):
        self.name = name
        self.dutch_game = dutch_game
        dutch_game.add_event_listener(self)

    def update_player_possible_moves(self, player_possible_moves):
        self.player_possible_moves = player_possible_moves

