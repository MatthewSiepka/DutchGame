from abc import abstractmethod, ABC


class SceneController(ABC):
    change_scene_function: any

    def bind_change_scene_function(self, change_scene_function):
        self.change_scene_function = change_scene_function

    @abstractmethod
    def init_controller(self):
        ...

    @abstractmethod
    def key_input(self, key):
        ...
