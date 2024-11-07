import random

from dutch.player_interface import PlayerInterface
from dutch_core.card.card import Card
from dutch_core.events.player_event import PlayerEvent
from dutch_core.events.player_event_response import PlayerEventResponse
from dutch_core.player_move import PlayerMove


class AIPlayerInterface(PlayerInterface):
    event_handler: any
    start_game_handler: any
    own_cards: list[Card | None]

    def __init__(self):
        super().__init__("Jeffrey Bezos AI")
        self.own_cards = [None, None, None, None]

    def bind_game_interface(self, event_handler):
        self.event_handler = event_handler

    def move(self, move: PlayerEvent):
        self.event_handler(move)

    def ai_get_card_that_is_none(self):
        for i in range(len(self.own_cards)):
            if i is not None:
                return i
        return None

    def ai_look_at_own_cards(self):
        card = self.ai_get_card_that_is_none()
        self.look_at_own_cards(card)

    def get_card_with_higher_value(self, card: Card):
        for i, c in enumerate(self.own_cards):
            if c.card_value > card.card_value:
                return i
        return None

    def ai_jump_in(self):
        card_on_used_stack = self.last_game_event.change_on_board.card_on_used_stack
        for i, cards in enumerate(self.own_cards):
            if cards.card_rank == card_on_used_stack:
                self.jump_in(i)
                del self.own_cards[i]

    def ai_dutch(self):
        if self.ai_get_card_that_is_none() is None:
            value = 0
            for card in self.own_cards:
                value += card.card_value
            if value <= 4:
                self.dutch_game()

    def ai_look_at_any_cards(self):
        card = self.ai_get_card_that_is_none()
        if card is not None:
            self.look_at_cards(self.name, card)
        board = self.last_game_event.change_on_board
        player = board.players[random.randrange(0, len(board.players))]
        self.look_at_cards(player.player, random.randrange(0, player.cards))

    def event_listener(self, data: PlayerEventResponse):
        super().event_listener(data)
        if data.player_won is not None:
            return
        if PlayerMove.DUTCH in data.change_on_board.moves_possible:
            self.ai_dutch()
        if PlayerMove.LOOK_AT_ANY_CARDS in data.change_on_board.moves_possible:
            self.ai_look_at_any_cards()
        if data.player_event is not None:
            if data.player_event.player == self.name:
                if data.player_event.move == PlayerMove.LOOK_AT_OWN_CARDS:
                    self.own_cards[data.player_event.details.card] = data.details_for_player
                elif data.player_event.move == PlayerMove.TAKE_CARD_FROM_STACK:
                    card = self.ai_get_card_that_is_none()
                    if card is not None:
                        self.replace_card_from_own_stack(card)
                        self.own_cards[card] = data.details_for_player
                    else:
                        card_to_replace = self.get_card_with_higher_value(data.details_for_player)
                        if card_to_replace is None:
                            self.put_card_on_used_stack()
                        else:
                            self.replace_card_from_own_stack(card_to_replace)
                            self.own_cards[card_to_replace] = data.details_for_player

        if PlayerMove.LOOK_AT_OWN_CARDS in data.change_on_board.moves_possible:
            self.ai_look_at_own_cards()

        if PlayerMove.JUMP_IN in data.change_on_board.moves_possible:
            self.ai_jump_in()
        if PlayerMove.REARRANGE_PLACE_OF_CARDS:
            player = data.change_on_board.players[0].player
            self.rearrange_place_of_cards(player, 0, player, 0)

    def game_change_event_listener(self, players):
        self.players = players
