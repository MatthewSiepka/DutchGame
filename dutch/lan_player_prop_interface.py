import json
from socket import socket

from communication.ProTooCool.pro_too_cool_utils import send_data
from dutch.player_interface import PlayerInterface
from dutch_core.events.player_event import PlayerEvent, dict_to_player_event
from dutch_core.events.player_event_response import PlayerEventResponse, translate_player_event_response_to_json


class LanPlayerPropInterface(PlayerInterface):
    sock: socket
    event_handler: any

    def __init__(self, name: str, sock: socket, game_handler: any):
        super().__init__(name)
        self.sock = sock
        # self.game_interface = game_interface
        self.event_handler = game_handler

    def move(self, move: PlayerEvent):
        self.event_handler(move)

    def event_listener(self, data: PlayerEventResponse):
        self.last_game_event = data
        self.__handle_event_response(data)

    def __handle_event_response(self, event_response: PlayerEventResponse):
        data = translate_player_event_response_to_json(event_response)
        data = json.dumps(data)
        send_data(self.sock, data)

    def game_change_event_listener(self, players: list[str]):
        data = {
            "event": "PlayerUpdate",
            "players": players
        }
        data = json.dumps(data)
        send_data(self.sock, data)

    def client_event_listener(self, data):
        data = json.loads(data)
        if data["event"] == "PlayerEvent":
            player_event = dict_to_player_event(data)
            self.move(player_event)
