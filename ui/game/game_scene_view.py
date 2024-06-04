import curses

from dutch_core.card.card import Card
from dutch_core.events.player_info import PlayerInfo
from ui.game.game_scene_model import GameSceneModel
from ui.gui_utility.add_center_text import add_center_text
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
from ui.scene.scene_view import SceneView


class GameSceneView(SceneView):
    model: GameSceneModel

    def __init__(self, stdscr: curses.window, model: GameSceneModel):
        super().__init__(stdscr)
        self.model = model

    def is_active(self, mode_id: int):
        return curses.color_pair(2) if self.model.active == mode_id else curses.color_pair(3)

    def render_card(self, y: int, x: int, card: Card | None):
        self.stdscr.addstr(y, x, "_____", curses.color_pair(3))
        self.stdscr.addstr(y + 1, x, "|///|", curses.color_pair(3))
        self.stdscr.addstr(y + 2, x, "|///|", curses.color_pair(3))
        self.stdscr.addstr(y + 3, x, "-----", curses.color_pair(3))

        if card is not None:
            color = curses.color_pair(4) if card.card_color.value["color"] == "red" else curses.color_pair(3)
            self.stdscr.addstr(y + 1, x + 1, f"{card.card_color.value["icon"]} ", color)
            self.stdscr.addstr(y + 2, x + 1, f"{card.card_value} ")

    def render_card_deck(self, height_of_deck, player: PlayerInfo):
        height, width = self.stdscr.getmaxyx()
        card_length = 7
        cards_start = (width // 2) - (card_length * player.cards) // 2
        for i in range(player.cards):
            add_center_text(self.stdscr, player.player, height_of_deck, curses.color_pair(3))
            self.render_card(height_of_deck + 2, cards_start + card_length * i, None)

    def render_card_decks(self, height):
        board = self.model.player_interface.last_game_event.change_on_board
        for i, player in enumerate(board.players):
            self.render_card_deck(height + i * 9, player)

    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", 5, curses.A_BOLD | curses.COLOR_WHITE)
        self.render_card_decks(
            height // 2 - (9 * len(self.model.player_interface.last_game_event.change_on_board.players)) // 2
        )

