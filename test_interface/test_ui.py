from dutch_core.dutch_game import DutchGame
from dutch_core.player_interface import PlayerInterface
from dutch_core.player_move import PlayerMove
from dutch_core.events.player_event import DetailsOtherPlayerCard, DetailsCardId, DetailsForRearranging


class TestUI:
    game: DutchGame = None
    players: dict = {}

    def __init__(self, game: DutchGame, players: list[PlayerInterface]):
        self.game = game
        for player in players:
            self.players[player.name] = player

    def move_handler(self, data: str):
        data = data.split(";")
        name = data[0]
        move = data[1]
        print(self.players)
        print(name, move)
        player = self.players[name]
        details_str = None if len(data) <= 2 else data[2:]
        match move:
            case "look_at_own_cards":
                details = DetailsCardId(int(details_str[0]))
                player.request_event(PlayerMove.LOOK_AT_OWN_CARDS, details)
            case "look_at_any_cards":
                details = DetailsOtherPlayerCard(int(details_str[0]), details_str[1])
                player.request_event(PlayerMove.LOOK_AT_ANY_CARDS, details)
            case "rearrange_place_of_cards":
                details = DetailsForRearranging(details_str[0], details_str[1], int(details_str[2]), int(details_str[3]))
                player.request_event(PlayerMove.REARRANGE_PLACE_OF_CARDS, details)
            case "dutch":
                player.request_event(PlayerMove.DUTCH, None)
            case "take_card_from_stack":
                player.request_event(PlayerMove.TAKE_CARD_FROM_STACK, None)
            case "take_card_from_used_stack":
                player.request_event(PlayerMove.TAKE_CARD_FROM_USED_STACK, None)
            case "replace_card_from_own_deck":
                details = DetailsCardId(int(details_str[0]))
                player.request_event(PlayerMove.REPLACE_CARD_FROM_OWN_DECK, details)
            case "put_card_on_used_stack":
                player.request_event(PlayerMove.PUT_CARD_ON_USED_STACK, None)
