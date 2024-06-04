import curses
import socket

from dutch.lan_player_interface import LanPlayerInterface
from dutch_core.player_move import PlayerMove
from ui.game.game_scene_model import GameSceneModel, GameSelectionType
from ui.scene.scene_controller import SceneController


class GameSceneController(SceneController):
    model: GameSceneModel

    def __init__(self, model: GameSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def action_handler(self):
        board = self.model.player_interface.last_game_event.change_on_board
        if not len(board.moves_possible) == 0 or 0 <= self.model.actions_selected < len(board.moves_possible):
            if board.moves_possible[self.model.actions_selected] == PlayerMove.LOOK_AT_OWN_CARDS:
                self.model.game_selection = GameSelectionType.PLAYER_CARDS
                self.model.player_cards_selected = 0

    def go_back_to_actions(self):
        self.model.player_cards_selected = 0
        self.model.game_selection = GameSelectionType.ACTIONS
    def key_input(self, key):
        board = self.model.player_interface.last_game_event.change_on_board
        if self.model.game_selection == GameSelectionType.ACTIONS:
            if len(board.moves_possible) <= self.model.actions_selected:
                self.model.actions_selected = 0
            if key == curses.KEY_LEFT and self.model.actions_selected > 0:
                self.model.actions_selected -= 1
            if key == curses.KEY_RIGHT and self.model.actions_selected < len(board.moves_possible) - 1:
                self.model.actions_selected += 1
            if key == 10 and not len(board.moves_possible) == 0:
                if (
                        board.moves_possible[self.model.actions_selected] == PlayerMove.LOOK_AT_OWN_CARDS or
                        board.moves_possible[self.model.actions_selected] == PlayerMove.REPLACE_CARD_FROM_OWN_DECK or
                        board.moves_possible[self.model.actions_selected] == PlayerMove.JUMP_IN
                ):
                    self.model.game_selection = GameSelectionType.PLAYER_CARDS
                if board.moves_possible[self.model.actions_selected] == PlayerMove.DUTCH:
                    self.model.player_interface.dutch_game()
                if board.moves_possible[self.model.actions_selected] == PlayerMove.TAKE_CARD_FROM_STACK:
                    self.model.player_interface.take_card_from_stack()
                if board.moves_possible[self.model.actions_selected] == PlayerMove.TAKE_CARD_FROM_USED_STACK:
                    self.model.player_interface.take_card_from_used_stack()
                if board.moves_possible[self.model.actions_selected] == PlayerMove.PUT_CARD_ON_USED_STACK:
                    self.model.player_interface.put_card_on_used_stack()
            return
        if self.model.game_selection == GameSelectionType.PLAYER_CARDS:
            if board.player_cards <= self.model.player_cards_selected:
                self.model.player_cards_selected = 0
            if key == curses.KEY_LEFT and self.model.player_cards_selected > 0:
                self.model.player_cards_selected -= 1
            if key == curses.KEY_RIGHT and self.model.player_cards_selected < board.player_cards - 1:
                self.model.player_cards_selected += 1
            if key == 27:
                self.model.player_cards_selected = 0
                self.model.game_selection = GameSelectionType.ACTIONS
            if key == 10:
                if board.moves_possible[self.model.actions_selected] == PlayerMove.LOOK_AT_OWN_CARDS:
                    self.model.player_interface.look_at_own_cards(self.model.player_cards_selected)
                    self.go_back_to_actions()
                    return
                if board.moves_possible[self.model.actions_selected] == PlayerMove.REPLACE_CARD_FROM_OWN_DECK:
                    self.model.player_interface.replace_card_from_own_stack(self.model.player_cards_selected)
                    self.go_back_to_actions()
                    return
                if board.moves_possible[self.model.actions_selected] == PlayerMove.JUMP_IN:
                    self.model.player_interface.jump_in(self.model.player_cards_selected)
                    self.go_back_to_actions()
                    return


