from ui.lan_connection.lan_connection_scene import LanConnectionScene
from ui.mode_selector.mode_selector_scene import ModeSelectorScene
from ui.scene.gui_controller import GUIController
from ui.start_up.start_up_scene import StartUpScene


def ui(stdscr):
    gui = GUIController(stdscr)
    start_up_scene = StartUpScene(stdscr)
    mode_selector = ModeSelectorScene(stdscr)
    lan_connection_scene = LanConnectionScene(stdscr)
    gui.add_scene(start_up_scene)
    gui.add_scene(mode_selector)
    gui.add_scene(lan_connection_scene)
    gui.run()