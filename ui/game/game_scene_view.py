import curses
from curses.textpad import rectangle

from dutch_core.card.card import Card, CardsRank
from dutch_core.events.player_info import PlayerInfo
from dutch_core.game_change import GameChange
from dutch_core.player_move import player_move_to_text, PlayerMove
from ui.game.game_scene_model import GameSceneModel, GameSelectionType
from ui.gui_utility.add_center_text import add_center_text
from ui.gui_utility.card_render.card_redner import render_card
from ui.scene.scene_view import SceneView

class GameSceneView(SceneView):
    model: GameSceneModel

    def __init__(self, stdscr: curses.window, model: GameSceneModel):
        super().__init__(stdscr)
        self.model = model


    def render(self):
        height, width = self.stdscr.getmaxyx()
        add_center_text(self.stdscr, "Dutch Game", 0, curses.A_BOLD | curses.COLOR_WHITE)
