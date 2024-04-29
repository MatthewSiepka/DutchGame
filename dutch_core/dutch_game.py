from dataclasses import dataclass

from dutch_core.events.board import Board
from dutch_core.events.player_event import PlayerEvent, DetailsCardId, DetailsOtherPlayerCard, DetailsForRearranging
from dutch_core.events.player_info import PlayerInfo
from dutch_core.events.status import Status
from dutch_core.exceptins import IllegalMove
from dutch_core.game_change import GameChange
from dutch_core.player_move import PlayerMove
from dutch_core.events.player_event_response import PlayerEventResponse
from dutch_core.dutch_options import DutchOptions, DEFAULT_OPTIONS
from dutch_core.dutch_game_data import DutchGameData
from dutch_core.card.card import Card, CardsRank


@dataclass
class Player:
    name: str
    possible_moves: list[PlayerMove]
    event_listener: lambda e: PlayerEventResponse


class DutchGame:
    players: dict | None = {}
    players_order: list[Player] = []
    player_turn: None | int = None
    dutch: int | None = None
    options: DutchOptions
    game_data: DutchGameData
    player_won: None | str = None
    card_selected: Card | None = None

    def __init__(self, options=None):
        if options is None:
            options = DEFAULT_OPTIONS
        self.options = options

    def add_player(self, name: str, user_event_listener):
        name_player = Player(name, [], user_event_listener)
        self.players_order.append(name_player)
        self.players[name] = name_player

    def init_game(self):
        players_list = []
        for player in self.players_order:
            players_list.append({"name": player.name})
        self.game_data = DutchGameData(self.options.card_values, players_list)

    def deal_cards(self):
        for i in range(self.options.cards_on_start):
            for player in self.players_order:
                self.game_data.add_player_card(player.name, self.game_data.take_card_from_stack())
        for player in self.players_order:
            player.possible_moves = [PlayerMove.LOOK_AT_OWN_CARDS for _ in range(self.options.cards_to_check)]
        self.game_data.put_card_on_used_stack(self.game_data.take_card_from_stack())

    def start_game(self):
        self.init_game()
        self.deal_cards()
        self.send_event_to_players(None, game_change=GameChange.CARDS_DEALT)

    def remove_player_possible_move(self, player_name: str, move: PlayerMove):
        self.players[player_name].possible_moves.remove(move)

    def next_player_turn(self):
        if self.player_turn is None or self.player_turn == len(self.players_order) - 1:
            self.player_turn = 0
        else:
            self.player_turn += 1
        return not (self.dutch is not None and self.dutch == self.player_turn)

    def get_boards_for_players(self) -> list[Board]:
        player_boards = []
        players = [
            PlayerInfo(player.name, self.game_data.get_players_card_count(player.name))
            for player in self.players_order
        ]
        card_on_used_stack = self.game_data.look_at_card_on_used_stack()
        player_turn = None if self.player_turn is None else self.players_order[self.player_turn].name
        for index, player in enumerate(self.players_order):
            players_info_to_end = [] if index == 0 else players[:index]
            players_info_from_beginning = [] if index + 1 == len(players) else players[(index + 1):]
            players_info = players_info_from_beginning + players_info_to_end
            board = Board(
                card_on_used_stack,
                players_info,
                self.game_data.get_players_card_count(player.name),
                player_turn,
                player.possible_moves
            )
            player_boards.append(board)
        return player_boards

    def send_event_to_players(
            self,
            player_event: PlayerEvent | None,
            game_change: GameChange | None = None,
            status: Status = Status.SUCCESS,
            details_for_player: None | Card = None,
            jump_in_details: None | Card = None,
            message: None | str = None
    ):
        if status == Status.FAIL:
            response = PlayerEventResponse(status, game_change, player_event, None, None, None, self.player_won, message)
            self.players[player_event.player].event_listener(response)
            return
        player_board = self.get_boards_for_players()
        for index, player in enumerate(self.players_order):
            change_on_board = player_board[index]
            details_for_player = details_for_player if player_event is None or player.name == player_event.player else None
            response = PlayerEventResponse(
                status,
                game_change,
                player_event,
                details_for_player,
                change_on_board,
                jump_in_details,
                self.player_won,
                None
            )
            player.event_listener(response)

    def check_if_type_of_details_is_good(self,
                                         player_event: PlayerEvent,
                                         type_of_detail:
                                         type(DetailsCardId) |
                                         type(DetailsOtherPlayerCard) |
                                         type(DetailsForRearranging)
                                         ):
        if not isinstance(player_event.details, type_of_detail):
            raise IllegalMove(player_event.player, "Details are not type of DetailsCardId")

    def check_if_player_exists(self, player_event: PlayerEvent, player_name: str):
        if not player_name in self.players:
            raise IllegalMove(player_event, "Player with name: " + player_name + " does not exists")

    def look_at_own_cards(self, player_event: PlayerEvent):
        self.check_if_type_of_details_is_good(player_event, DetailsCardId)
        card = self.game_data.check_players_card(player_event.player, player_event.details.card)
        self.remove_player_possible_move(player_event.player, PlayerMove.LOOK_AT_OWN_CARDS)
        is_end_of_looking_faze = True
        for player in self.players_order:
            if not len(player.possible_moves) == 0:
                is_end_of_looking_faze = False
                break
        if is_end_of_looking_faze:
            self.set_up_next_players_turn()

        self.send_event_to_players(player_event, details_for_player=card)

    def set_up_next_players_turn(self):
        self.next_player_turn()
        for index, player in enumerate(self.players_order):
            if index == self.player_turn:
                player.possible_moves = [
                    PlayerMove.TAKE_CARD_FROM_STACK,
                    PlayerMove.TAKE_CARD_FROM_USED_STACK,
                ]
                if self.dutch is None:
                    player.possible_moves.append(PlayerMove.DUTCH)
            else:
                player.possible_moves = [PlayerMove.JUMP_IN]

    def look_at_any_cards(self, player_event: PlayerEvent):
        self.check_if_type_of_details_is_good(player_event, DetailsOtherPlayerCard)
        if player_event.details.player not in self.players:
            raise IllegalMove(player_event.player, "Player Does not exists")
        card = self.game_data.check_players_card(player_event.details.player, player_event.details.card)
        self.set_up_next_players_turn()
        self.send_event_to_players(player_event, details_for_player=card)

    def check_if_player_index_exist(self, player_event: PlayerEvent, player_name: str, card_id: int):
        if not card_id >= 0 and self.game_data.get_players_card_count(player_name) < card_id:
            raise IllegalMove(player_event.player, f"Card: {card_id} id is out of Range in {player_name} Deck")

    def rearrange_place_of_cards(self, player_event: PlayerEvent):
        self.check_if_type_of_details_is_good(player_event, DetailsForRearranging)
        self.check_if_player_exists(player_event, player_event.details.player_one)
        self.check_if_player_exists(player_event, player_event.details.player_two)
        details = player_event.details
        self.check_if_player_index_exist(player_event, details.player_one, details.player_one_card)
        self.check_if_player_index_exist(player_event, details.player_two, details.player_two_card)
        self.game_data.rearrange_players_cards(
            details.player_one,
            details.player_one_card,
            details.player_two,
            details.player_two_card
        )
        self.set_up_next_players_turn()
        self.send_event_to_players(player_event)

    def perform_dutch(self, player_event: PlayerEvent):
        self.dutch = self.player_turn
        self.remove_player_possible_move(self.players_order[self.player_turn].name, PlayerMove.DUTCH)
        self.send_event_to_players(player_event)

    def jump_in(self, player_event: PlayerEvent):
        ...

    def take_card_from_stack(self, player_event: PlayerEvent):
        card = self.game_data.take_card_from_stack()
        self.card_selected = card
        player = self.players_order[self.player_turn]
        player.possible_moves = [PlayerMove.REPLACE_CARD_FROM_OWN_DECK, PlayerMove.PUT_CARD_ON_USED_STACK]
        self.send_event_to_players(player_event)

    def take_card_from_used_stack(self, player_event: PlayerEvent):
        card = self.game_data.take_card_from_used_stack()
        self.card_selected = card
        player = self.players[player_event.player]
        player.possible_moves = [PlayerMove.REPLACE_CARD_FROM_OWN_DECK]
        self.send_event_to_players(player_event)

    def put_card_on_used_stack(self, player_event: PlayerEvent, from_own_deck: bool = False):
        special_card = False
        if from_own_deck:
            if self.card_selected.card_rank == CardsRank.QUEEN:
                self.players[player_event.player].possible_moves = [PlayerMove.LOOK_AT_ANY_CARDS]
                special_card = True
            elif self.card_selected.card_rank == CardsRank.JACK:
                self.players[player_event.player].possible_moves = [PlayerMove.REARRANGE_PLACE_OF_CARDS]
                special_card = True
        self.game_data.put_card_on_used_stack(self.card_selected)
        self.card_selected = None
        if not special_card:
            self.set_up_next_players_turn()
        self.send_event_to_players(player_event)

    def replace_card_from_own_deck(self, player_event: PlayerEvent):
        self.check_if_type_of_details_is_good(player_event, DetailsCardId)
        self.check_if_player_index_exist(player_event, player_event.player, player_event.details.card)
        self.card_selected = self.game_data.replace_players_card(
            player_event.player,
            self.card_selected,
            player_event.details.card
        )
        self.put_card_on_used_stack(player_event, True)

    def perform_player_event(self, player_event: PlayerEvent):
        match player_event.move:
            case PlayerMove.LOOK_AT_OWN_CARDS:
                self.look_at_any_cards(player_event)
            case PlayerMove.LOOK_AT_ANY_CARDS:
                self.look_at_any_cards(player_event)
            case PlayerMove.REARRANGE_PLACE_OF_CARDS:
                self.rearrange_place_of_cards(player_event)
            case PlayerMove.DUTCH:
                self.perform_dutch(player_event)
            case PlayerMove.JUMP_IN:
                self.jump_in(player_event)
            case PlayerMove.TAKE_CARD_FROM_STACK:
                self.take_card_from_used_stack(player_event)
            case PlayerMove.TAKE_CARD_FROM_USED_STACK:
                self.take_card_from_used_stack(player_event)
            case PlayerMove.REPLACE_CARD_FROM_OWN_DECK:
                self.replace_card_from_own_deck(player_event)
            case PlayerMove.PUT_CARD_ON_USED_STACK:
                self.put_card_on_used_stack(player_event)

    def player_input(self, player_event: PlayerEvent):
        player_name = player_event.player
        try:
            self.check_if_player_exists(player_event, player_name)
            if player_event.move not in self.players[player_name].possible_moves:
                raise IllegalMove(player_name, "player can't perform this move")
            self.perform_player_event(player_event)
        except IllegalMove as err:
            self.send_event_to_players(player_event, status=Status.FAIL, message=str(err))
