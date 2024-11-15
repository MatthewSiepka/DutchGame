import curses
from abc import ABC, abstractmethod

from ui.scene.scene_controller import SceneController
from ui.scene.scene_view import SceneView


class Scene(ABC):
    name: str
    scene_controller: SceneController
    scene_view: SceneView
    stdscr: curses.window
    change_scene: any

    def __init__(self, stdscr: curses.window):
        self.stdscr = stdscr

    @abstractmethod
    def change_scene_listener(self, args):
        ...

    def get_view(self):
        ...

    def render(self):
        self.scene_view.render()

    def bind_change_scene(self, change_scene):
        self.change_scene = change_scene
        self.scene_controller.bind_change_scene_function(change_scene)
