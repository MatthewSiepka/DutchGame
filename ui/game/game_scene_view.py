import curses
from curses.textpad import rectangle

from dutch_core.card.card import Card, CardsRank
from dutch_core.events.player_info import PlayerInfo
from dutch_core.game_change import GameChange
from dutch_core.player_move import player_move_to_text, PlayerMove
from ui.game.game_scene_model import GameSceneModel, GameSelectionType
from ui.gui_utility.add_center_text import add_center_text
from ui.scene.scene_view import SceneView


class GameSceneView(SceneView):
    model: GameSceneModel

    def __init__(self, stdscr: curses.window, model: GameSceneModel):
        super().__init__(stdscr)
        self.model = model

    def render_card(self, y: int, x: int, card: Card | None, color):
        self.stdscr.addstr(y, x, "_____", color)
        self.stdscr.addstr(y + 1, x, "|///|", color)
        self.stdscr.addstr(y + 2, x, "|///|", color)
        self.stdscr.addstr(y + 3, x, "-----", color)

        if card is not None:
            color = curses.color_pair(4) if card.card_color.value["color"] == "red" else curses.color_pair(3)
            self.stdscr.addstr(y + 1, x + 1, f"{card.card_color.value["icon"]}  ", color)
            self.stdscr.addstr(y + 2, x + 1,
                               f"{card.card_rank.value}{" " if card.card_rank == CardsRank.TEN else "  "}")

    def render_card_deck(self, height_of_deck, player: PlayerInfo, witch_one: int):
        height, width = self.stdscr.getmaxyx()
        card_length = 6
        half_of_deck_width = card_length * player.cards // 2
        cards_start = ((width // 2) - half_of_deck_width)
        game_event = self.model.player_interface.last_game_event
        if self.model.game_selection == GameSelectionType.ALL_CARDS and self.model.player_selected == witch_one:
            rectangle(
                self.stdscr,
                height_of_deck - 1,
                cards_start - 2,
                height_of_deck + 6,
                width // 2 + half_of_deck_width
            )
        for i in range(player.cards):
            color = curses.color_pair(3)
            card = None
            if player.player == "Your deck:":
                if (
                        (self.model.game_selection == GameSelectionType.PLAYER_CARDS and
                         self.model.player_cards_selected == i)
                ):
                    color = curses.color_pair(2)

                if (
                        game_event.details_for_player is not None and
                        game_event.player_event.move == PlayerMove.LOOK_AT_OWN_CARDS and
                        game_event.player_event.details.card == i
                ):
                    card = game_event.details_for_player

            if (
                    (self.model.game_selection == GameSelectionType.ALL_CARDS_SELECTION
                     and self.model.player_selected == witch_one
                     and self.model.player_cards_selected == i) or
                    (self.model.all_cards_selected is not None and
                     witch_one == self.model.all_cards_selected[0] and
                     i == self.model.all_cards_selected[1])

            ):
                color = curses.color_pair(2)
            if (
                    game_event.details_for_player is not None and
                    game_event.player_event.move == PlayerMove.LOOK_AT_ANY_CARDS and
                    (game_event.player_event.details.player == player.player or
                     game_event.player_event.details.player == self.model.player_interface.name)
                    and game_event.player_event.details.card == i
            ):
                card = game_event.details_for_player

            self.render_card(height_of_deck + 3, cards_start + card_length * i, card, color)
        add_center_text(self.stdscr, player.player, height_of_deck, curses.color_pair(3))

    def render_card_decks(self, height):
        board = self.model.player_interface.last_game_event.change_on_board
        for i, player in enumerate(board.players):
            self.render_card_deck(height + i * 9, player, len(board.players) - i)

    def is_active(self, active_id: int, id_of_component: int):
        return curses.color_pair(2) if active_id == id_of_component else curses.color_pair(3)

    def get_player_card_row(self, player: str):
        last_event = self.model.player_interface.last_game_event
        if player == "Your deck:" or player == self.model.player_interface.name:
            return 0
        for i, other_player in last_event.change_on_board.players:
            if other_player.name == player:
                return i
        return None

    def render_user_move(self, height: int):
        game_event = self.model.player_interface.last_game_event
        if game_event.player_event is None or game_event.player_event.player == self.model.player_interface.name:
            return
        message = game_event.player_event.player
        player_event = game_event.player_event
        match player_event.move:
            case PlayerMove.LOOK_AT_OWN_CARDS:
                message += f" have looked at {str(player_event.details.card)} card"
            case PlayerMove.LOOK_AT_ANY_CARDS:
                message += f" have looked at {player_event.details.player}'s {str(player_event.details.card)} card"
            case PlayerMove.REARRANGE_PLACE_OF_CARDS:
                message += f" have rearranged "
                message += f"{player_event.details.player_one}'s {str(player_event.details.player_one_card)} card with "
                message += f"{player_event.details.player_two}'s {str(player_event.details.player_two_card)} card"
            case PlayerMove.DUTCH:
                message += f" have duched!"
            case PlayerMove.JUMP_IN:
                message += f" have Jumped In with {str(player_event.details.card)} card"
            case PlayerMove.TAKE_CARD_FROM_STACK:
                message += " took card from stack"
            case PlayerMove.TAKE_CARD_FROM_USED_STACK:
                message += " took card from used stack"
            case PlayerMove.REPLACE_CARD_FROM_OWN_DECK:
                message += f" have replaced his {str(player_event.details.card)} card"
            case PlayerMove.PUT_CARD_ON_USED_STACK:
                message += f" putted card on used stack"
        add_center_text(self.stdscr, message, height, curses.color_pair(3))

    def render_moves_possible(self, height):
        y_and_x = self.stdscr.getmaxyx()
        board = self.model.player_interface.last_game_event.change_on_board
        moves_in_text = []
        over_all_length = 0
        for move_possible in board.moves_possible:
            move_in_text = player_move_to_text(move_possible)
            over_all_length += len(move_in_text) + 6
            moves_in_text.append(move_in_text)

        start_of_actions = (y_and_x[1] - 1) // 2 - (over_all_length + len(moves_in_text) - 1) // 2

        start = start_of_actions
        for i, moves_possible in enumerate(moves_in_text):
            self.stdscr.addstr(height, start, " | " + moves_possible + " | ",
                               self.is_active(self.model.actions_selected, i))
            start += len(moves_possible) + 6

    def render_utility_card_row(self, height):
        last_event = self.model.player_interface.last_game_event
        y_and_x = self.stdscr.getmaxyx()
        # stack card
        stack_card_label = "stack"
        self.stdscr.addstr(height, y_and_x[1] // 2 - 12 - len(stack_card_label) // 2, stack_card_label,
                           curses.color_pair(3))
        self.render_card(height + 1, y_and_x[1] // 2 - 5 // 2 - 12, None, curses.color_pair(3))
        # card selected
        selected_card = last_event.details_for_player \
            if (last_event.player_event is not None and
                not last_event.player_event.move == PlayerMove.LOOK_AT_OWN_CARDS) \
            else None
        used_stack_label = "selected"
        self.stdscr.addstr(height, y_and_x[1] // 2 - len(used_stack_label) // 2, used_stack_label, curses.color_pair(3))
        self.render_card(height + 1, y_and_x[1] // 2 - 5 // 2, selected_card, curses.color_pair(3))
        used_stack_label = "used stack"
        # used stack card
        used_stack_card = last_event.change_on_board.card_on_used_stack
        self.stdscr.addstr(height, y_and_x[1] // 2 + 12 - len(used_stack_label) // 2, used_stack_label,
                           curses.color_pair(3))
        self.render_card(height + 1, y_and_x[1] // 2 - 5 // 2 + 12, used_stack_card, curses.color_pair(3))

    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", 0, curses.A_BOLD | curses.COLOR_WHITE)
        if (self.model.player_interface.last_game_event.game_change is GameChange.END_OF_GAME or
                self.model.player_interface.last_game_event.change_on_board is None):
            add_center_text(self.stdscr,
                            f"Player {self.model.player_interface.last_game_event.player_won} wins!",
                            height // 2, curses.color_pair(3))

            return
        else:
            board = self.model.player_interface.last_game_event.change_on_board
            self.render_user_move(2)
            add_center_text(self.stdscr,
                            f"turn: {board.player_turn if board.player_turn is not None else "no one's turn"}",
                            4,
                            curses.A_BOLD | curses.COLOR_WHITE)
            self.render_card_decks(7)
            player = PlayerInfo("Your deck:", self.model.player_interface.last_game_event.change_on_board.player_cards)
            self.render_utility_card_row(height - 16)
            self.render_card_deck(height - 10, player, 0)
            self.render_moves_possible(height - 2)
