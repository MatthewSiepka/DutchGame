from dutch.player_interface import PlayerInterface
from dutch_core.events.player_event import PlayerEvent
from dutch_core.events.player_event_response import PlayerEventResponse


class HostPlayerInterface(PlayerInterface):
    event_handler: any
    start_game_handler: any
    # first_update: bool

    def __init__(self, name):
        super().__init__(name)

    def bind_game_interface(self, event_handler, start_game_handler):
        self.event_handler = event_handler

    def move(self, move: PlayerEvent):
        self.event_handler(move)
        ...

    def event_listener(self, data: PlayerEventResponse):
        super().event_listener(data)

    def game_change_event_listener(self, players):
        self.players = players
        ...

    def start_game(self):
        if len(self.players) > 0:
            self.start_game_handler()
