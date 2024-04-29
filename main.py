from dutch_core.player_move import PlayerMove
from dutch_core.dutch_game import DutchGame

game = DutchGame()
game.add_player("test", lambda a: print(a))
game.add_player("test2", lambda a: print(a))
game.start_game()

print(game.get_boards_for_players())
