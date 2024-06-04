import json

from communication.client import Client
from dutch.player_interface import PlayerInterface
from dutch_core.events.player_event import PlayerEvent, player_event_to_dict
from dutch_core.events.player_event_response import PlayerEventResponse

"""
{
    "event": "PlayersUpdate",
    "players": ["player", "player", "player"]
}
"""


class LanPlayerInterface(PlayerInterface):
    client: Client
    update_ui: any

    def __init__(self, name: str, host: str, port: int):
        super().__init__(name)
        self.client = Client(host, port, self.event_listener)
        self.__send_init_message()
        self.event_handler = self.move

    def __send_init_message(self):
        data_to_send = {"event": "NewUser", "name": self.name}
        data_to_send = json.dumps(data_to_send)
        self.client.send_message_to_server(data_to_send)

    def move(self, move: PlayerEvent):
        data = player_event_to_dict(move)
        data = json.dumps(data)
        self.client.send_message_to_server(data)

    def game_change_event_listener(self, players):
        super().game_change_event_listener(players)
        ...

    def handle_event_response(self, event_response: PlayerEventResponse):
        self.last_game_event = event_response

    def server_event_listener(self, data: str):
        event = json.loads(data)
        match event["event"]:
            case "PlayerUpdate":
                self.update_player_list(event)
            case "GameEvent":
                ...

    def event_listener(self, data: PlayerEventResponse):
        ...

    def update_player_list(self, data: dict):
        self.players = data["players"]
        self.update_ui()
        ...
