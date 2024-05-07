from dutch_core.dutch_game import DutchGame
from dutch_core.events.board import Board
from dutch_core.events.player_event_response import PlayerEventResponse
from dutch_core.player_move import PlayerMove
from dutch_core.events.player_event import DetailsOtherPlayerCard, DetailsCardId, DetailsForRearranging, PlayerEvent


class PlayerInterface:
    name: str | None = None
    dutch_game: DutchGame | None = None
    board: Board | None = None

    def __init__(self, name, dutch_game: DutchGame):
        self.name = name
        self.dutch_game = dutch_game
        self.dutch_game.add_player(name, lambda e: self.event_handler(e))

    def show_board(self):
        for player in self.board.players:
            if self.board.player_turn == player.player:
                print("Player Turn:")
            print("Player:", player.player, "cards:")
            for _ in range(player.cards):
                print("|| ", end="")
            print()
        print()
        print("Player cards: ")
        for _ in range(self.board.player_cards):
            print("|| ", end="")
        print()
        print("card on used stack:")
        print(self.board.card_on_used_stack)
        print()
        print("your possible moves:")
        print(self.board.moves_possible)

    def event_handler(self, player_event_response: PlayerEventResponse):
        print(player_event_response)
        if player_event_response.change_on_board is not None:
            board = player_event_response.change_on_board
            self.board = board
        if self.board is not None:
            self.show_board()
        if player_event_response.details_for_player is not None:
            print("Card checked: ")
            print(player_event_response.details_for_player)

    def request_event(self, player_move: PlayerMove, details: None | DetailsCardId | DetailsOtherPlayerCard | DetailsForRearranging):
        player_event = PlayerEvent(self.name, player_move, details)
        self.dutch_game.player_input(player_event)