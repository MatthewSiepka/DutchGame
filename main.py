# from dutch_core.player_interface import PlayerInterface
# from dutch_core.dutch_game import DutchGame
# from test_interface.test_ui import TestUI
#
# game_old = DutchGame()
# player_one = PlayerInterface("test1", game_old)
# player_two = PlayerInterface("test2", game_old)
# players = [player_one, player_two]
#
# ui = TestUI(game_old, players)
# game_old.start_game()
#
# while(True):
#     userInput = input("PlayerName;Move;Details")
#     ui.move_handler(userInput)
from curses import wrapper

from ui.user_interface import ui

# from ui import user_interface
import locale
locale.setlocale(locale.LC_ALL, '')


wrapper(ui)
# UIMode("test")