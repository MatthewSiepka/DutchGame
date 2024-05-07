from dutch_core.player_interface import PlayerInterface
from dutch_core.player_move import PlayerMove
from dutch_core.dutch_game import DutchGame
from dutch_core.events.player_event import PlayerEvent, DetailsCardId
from test_interface.test_ui import TestUI

game = DutchGame()
player_one = PlayerInterface("test1", game)
player_two = PlayerInterface("test2", game)
players = [player_one, player_two]

ui = TestUI(game, players)
game.start_game()

while(True):
    userInput = input("PlayerName;Move;Details")
    ui.move_handler(userInput)