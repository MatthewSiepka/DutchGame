import curses

from dutch.ai_player_interface import AIPlayerInterface
from dutch.game_interface import GameInterface, GameInterfaceModes
from dutch.host_player_interface import HostPlayerInterface
from ui.mode_selector.mode_selector_scene_model import ModeSelectorSceneModel
from ui.scene.scene_controller import SceneController


class ModeSelectorSceneController(SceneController):
    model: ModeSelectorSceneModel

    def __init__(self, model: ModeSelectorSceneModel):
        self.model = model

    def change_scene_listener(self, *args):
        self.model.name = args[0]

    def init_controller(self):
        pass

    def key_input(self, key):
        if key == curses.KEY_DOWN and not self.model.active == 1:
            self.model.active += 1
        if key == curses.KEY_UP and not self.model.active == 0:
            self.model.active -= 1
        if key == 10:
            if self.model.active == 1:
                self.change_scene_function("lan_connection", self.model.name)
            if self.model.active == 0:
                host = HostPlayerInterface(self.model.name)
                game = GameInterface(host, GameInterfaceModes.LAN)
                self.change_scene_function("waiting_room", host, game)
            # if self.model.active == 2:
            #     host = HostPlayerInterface(self.model.name)
            #     ai = AIPlayerInterface()
            #     game_old = GameInterface(host, GameInterfaceModes.LOCAL)
            #     game_old.players_add_player(ai)
            #     game_old.start_lan_game()
            #     self.change_scene_function("game_old", game_old)

