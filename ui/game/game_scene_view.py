import curses

from dutch_core.card.card import Card, CardsRank
from dutch_core.events.player_info import PlayerInfo
from dutch_core.player_move import player_move_to_text, PlayerMove
from ui.game.game_scene_model import GameSceneModel, GameSelectionType
from ui.gui_utility.add_center_text import add_center_text
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
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
            self.stdscr.addstr(y + 2, x + 1, f"{card.card_rank.value}{" " if card.card_rank == CardsRank.TEN else "  "}")

    def render_card_deck(self, height_of_deck, player: PlayerInfo):
        height, width = self.stdscr.getmaxyx()
        card_length = 7
        cards_start = (width // 2) - (card_length * player.cards) // 2
        game_event = self.model.player_interface.last_game_event
        for i in range(player.cards):
            color = curses.color_pair(3)
            card = None
            if player.player == "Your deck:":
                if (
                    self.model.game_selection == GameSelectionType.PLAYER_CARDS and
                    self.model.player_cards_selected == i
                ):
                    color = curses.color_pair(2)
                if (
                        game_event.details_for_player is not None and
                        game_event.player_event.move == PlayerMove.LOOK_AT_OWN_CARDS and
                        game_event.player_event.details.card == i
                ):
                    card = game_event.details_for_player
            self.render_card(height_of_deck + 2, cards_start + card_length * i, card, color)
        add_center_text(self.stdscr, player.player, height_of_deck, curses.color_pair(3))

    def render_card_decks(self, height):
        board = self.model.player_interface.last_game_event.change_on_board
        for i, player in enumerate(board.players):
            self.render_card_deck(height + i * 9, player)

    def is_active(self, active_id: int, id_of_component: int):
        return curses.color_pair(2) if active_id == id_of_component else curses.color_pair(3)

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
        y_and_x = self.stdscr.getmaxyx()

    def render(self):
        height, width = self.stdscr.getmaxyx()
        board = self.model.player_interface.last_game_event.change_on_board
        add_center_text(self.stdscr, "Dutch Game", 0, curses.A_BOLD | curses.COLOR_WHITE)
        add_center_text(self.stdscr,
                        f"turn: {board.player_turn if board.player_turn is not None else "no one's turn"}",
                        3,
                        curses.A_BOLD | curses.COLOR_WHITE)
        self.render_card_decks(7)
        player = PlayerInfo("Your deck:", self.model.player_interface.last_game_event.change_on_board.player_cards)

        self.render_card_deck(height - 10, player)
        self.render_moves_possible(height - 2)
