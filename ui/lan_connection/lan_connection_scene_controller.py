import curses
import socket

from dutch.lan_player_interface import LanPlayerInterface
from ui.lan_connection.lan_connection_scene_model import LanConnectionSceneModel
from ui.scene.scene_controller import SceneController
from ui.start_up.start_up_scene_model import StartUpSceneModel


class LanConnectionSceneController(SceneController):
    model: LanConnectionSceneModel

    def __init__(self, model: LanConnectionSceneModel):
        self.model = model

    def init_controller(self):
        pass

    def key_input(self, key):
        if (
                self.model.active == 0 and (
                (ord("0") <= key <= ord("9")) or
                (ord("a") <= key <= ord("z")) or
                (ord("A") <= key <= ord("a")) or
                (key == ord(".")))
        ):
            self.model.host += chr(key)

        if ord("0") <= key <= ord("9") and self.model.active == 1:
            self.model.port += chr(key)

        if key == 127 and len(self.model.host) > 0:
            if self.model.active == 0:
                self.model.host = self.model.host[:-1]
            if self.model.active == 1:
                self.model.port = self.model.port[:-1]

        if key == curses.KEY_DOWN and not self.model.active == 1:
            self.model.active += 1
        if key == curses.KEY_UP and not self.model.active == 0:
            self.model.active -= 1

        if key == 10:
            if len(self.model.port) > 0 and len(self.model.host) > 0:
                try:
                    player = LanPlayerInterface(self.model.name, self.model.host, int(self.model.port))
                    self.change_scene_function("waiting_room", player)
                    self.model.error = ""
                except socket.error as e:
                    self.model.error = str(e)

                # self.change_scene_function("mode_selector", self.model.name)
