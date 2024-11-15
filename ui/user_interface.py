from ui.game.game_scene import GameScene
from ui.lan_connection.lan_connection_scene import LanConnectionScene
from ui.mode_selector.mode_selector_scene import ModeSelectorScene
from ui.scene.gui_controller import GUIController
from ui.start_up.start_up_scene import StartUpScene
from ui.waiting_room.waiting_room_scene import WaitingRoomScene


def ui(stdscr):
    gui = GUIController(stdscr)
    start_up_scene = StartUpScene(stdscr)
    mode_selector = ModeSelectorScene(stdscr)
    lan_connection_scene = LanConnectionScene(stdscr)
    waiting_room = WaitingRoomScene(stdscr)
    board = GameScene(stdscr)
    gui.add_scene(start_up_scene)
    gui.add_scene(mode_selector)
    gui.add_scene(lan_connection_scene)
    gui.add_scene(waiting_room)
    gui.add_scene(board)
    gui.run()
