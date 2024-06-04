import json
from enum import Enum, auto
from socket import socket

from communication.server import Server
from dutch.host_player_interface import HostPlayerInterface
from dutch.lan_player_prop_interface import LanPlayerPropInterface
from dutch.player_interface import PlayerInterface
from dutch_core.dutch_game import DutchGame
from dutch_core.events.player_event import PlayerEvent


class GameInterfaceModes(Enum):
    LOCAL = auto()
    LAN = auto()


class GameInterface():
    players: list[PlayerInterface]
    host: HostPlayerInterface
    mode: GameInterfaceModes
    server: Server | None
    game: DutchGame | None

    def __init__(self, host: HostPlayerInterface, mode: GameInterfaceModes):
        self.host = host
        self.host.bind_game_interface(self.move, self.start_lan_game)
        self.players = []
        self.inform_all_players_about_players_update()
        self.mode = mode
        self.game = None
        self.set_up_server()

    def set_up_server(self):
        if not self.mode == GameInterfaceModes.LAN:
            return
        self.server = Server(self.lan_event_listener)

    def lan_event_listener(self, conn: socket, addr, data):
        data = json.loads(data)
        if not data["event"] == "NewUser":
            conn.close()
        player = LanPlayerPropInterface(data["name"], conn, self.move)
        self.server.bind_evnet_listener(addr, player.client_event_listener)
        self.inform_all_players_about_players_update()

    def players_update(self):
        players = [self.host.name]
        for player in self.players:
            players.append(player.name)
        return players

    def inform_all_players_about_players_update(self):
        self.host.game_change_event_listener(self.players_update())

    def start_lan_game(self):
        self.game = DutchGame()
        self.game.add_player(self.host.name, self.host.event_listener)
        for player in self.players:
            self.game.add_player(player.name, player.event_listener)
        self.game.start_game()

    def move(self, move: PlayerEvent):
        self.game.player_input(move)
