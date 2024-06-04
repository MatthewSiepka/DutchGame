import _curses
import curses
import time

from ui.gui_utility.color_scheme import init_color_scheme
from ui.scene.scene import Scene


class GUIController:
    scenes: list[Scene]
    active_scene: int
    quit: bool
    stdscr: curses.window

    def __init__(self, stdscr: curses.window):
        self.stdscr = stdscr
        self.scenes = []
        self.stdscr.nodelay(True)
        curses.start_color()
        init_color_scheme()
        curses.curs_set(0)
        self.active_scene = 0
        self.quit = False

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)
        scene.bind_change_scene(self.change_scene)

    def change_scene(self, name: str, *args):
        for i, o in enumerate(self.scenes):
            if o.name == name:
                self.active_scene = i
                self.scenes[i].change_scene_listener(args)

    def run(self):
        while not self.quit:
            self.stdscr.clear()
            active_scene = self.scenes[self.active_scene]
            dementions = self.stdscr.getmaxyx()
            self.stdscr.addstr(dementions[0] - 1, 0, "press ^X to exit")
            active_scene.render()
            key = self.stdscr.getch()
            if key == 24:
                self.quit = True
            active_scene.scene_controller.key_input(key)
            time.sleep(1/30)


