from abc import ABC, abstractmethod

from dutch_core.events.player_event import DetailsForRearranging, DetailsOtherPlayerCard, PlayerEvent, DetailsCardId
from dutch_core.events.player_event_response import PlayerEventResponse
from dutch_core.game_change import GameChange
from dutch_core.player_move import PlayerMove


class PlayerInterface(ABC):
    name: str
    last_game_event: PlayerEventResponse | None
    players: [str]
    start_game_event: any

    def __init__(self, name):
        self.name = name
        self.last_event = None
        self.players = []

    @abstractmethod
    def move(self, move: PlayerEvent):
        ...

    def init_start_game_event(self, start_game_event):
        self.start_game_event = start_game_event

    @abstractmethod
    def event_listener(self, data: PlayerEventResponse):
        self.last_game_event = data
        if self.last_game_event.game_change == GameChange.CARDS_DEALT:
            self.start_game_event()

    @abstractmethod
    def game_change_event_listener(self, players: list[str]):
        self.players = players
        ...

    def __move(self, move: PlayerMove, details: DetailsCardId | DetailsOtherPlayerCard | DetailsForRearranging | None):
        player_event = PlayerEvent(self.name, move, details)
        self.move(player_event)

    def look_at_own_cards(self, card: int):
        self.__move(PlayerMove.LOOK_AT_OWN_CARDS, DetailsCardId(card))

    def look_at_cards(self, player: str, card: int):
<<<<<<< Updated upstream
        self.__move(PlayerMove.LOOK_AT_OWN_CARDS, DetailsOtherPlayerCard(card, player))
=======
        self.__move(PlayerMove.LOOK_AT_ANY_CARDS, DetailsOtherPlayerCard(card, player))
>>>>>>> Stashed changes

    def rearrange_place_of_cards(self, player_one: str, player_one_card: int, player_two: str, player_two_card: int):
        self.__move(
            PlayerMove.REARRANGE_PLACE_OF_CARDS,
            DetailsForRearranging(player_one, player_two, player_one_card, player_two_card)
        )

    def jump_in(self, card: int):
        self.__move(PlayerMove.JUMP_IN, DetailsCardId(card))

    def take_card_from_stack(self):
        self.__move(PlayerMove.TAKE_CARD_FROM_STACK, None)

    def take_card_from_used_stack(self):
        self.__move(PlayerMove.TAKE_CARD_FROM_USED_STACK, None)

    def replace_card_from_own_stack(self, card: int):
        self.__move(PlayerMove.REPLACE_CARD_FROM_OWN_DECK, DetailsCardId(card))

    def put_card_on_used_stack(self):
        self.__move(PlayerMove.PUT_CARD_ON_USED_STACK, None)

    def dutch_game(self):
        self.__move(PlayerMove.DUTCH, None)