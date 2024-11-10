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

        self.model.host_input.input_key(key)
        self.model.port_input.input_key(key)

        if key == curses.KEY_DOWN and not self.model.active == 1:
            self.model.active += 1
            self.set_active()
            return
        if key == curses.KEY_UP and not self.model.active == 0:
            self.model.active -= 1
            self.set_active()
            return

        if key == 10:
            host = self.model.host_input.text
            port = self.model.port_input.text

            if len(host) > 0 and len(port) > 0:
                try:
                    player = LanPlayerInterface(self.model.name, host, int(port))
                    self.change_scene_function("waiting_room", player)
                    self.model.error = ""
                except socket.error as e:
                    self.model.error = str(e)
            else:
                self.model.error = "Host and port inputs can't be empty!"
                # self.change_scene_function("mode_selector", self.model.name)

    def set_active(self):
        self.model.host_input.set_active(self.model.active == 0)
        self.model.port_input.set_active(self.model.active == 1)