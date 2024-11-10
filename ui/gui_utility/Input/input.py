import curses
from enum import Enum

from ui.gui_utility.Input.blinking_cursor import BlinkingCursor
from ui.gui_utility.add_center_text import add_center_text
from ui.gui_utility.color_scheme import curses_colors


class AcceptableCharacters(Enum):
    LETTERS = 0b100
    NUMBERS = 0b010
    SPECIAL_CHARACTERS = 0b001
    ALL = 0b111


class Input:
    __cursor: BlinkingCursor
    __stdscr: curses.window
    __active: bool
    __acceptable_characters: AcceptableCharacters
    text: str

    def __init__(self, stdscr, acceptable_characters: AcceptableCharacters):
        self.__stdscr = stdscr
        self.__cursor = BlinkingCursor(stdscr)
        self.__active = False
        self.text = ""
        self.__acceptable_characters = acceptable_characters

    def input_key(self, key: int):
        if not self.__active:
            return

        acceptable_character = self.__acceptable_characters.value

        if not acceptable_character & AcceptableCharacters.SPECIAL_CHARACTERS.value == 0 and (
                key == ord(" ") or key == ord(".")):
            self.text += chr(key)
            return

        if not acceptable_character & AcceptableCharacters.SPECIAL_CHARACTERS.LETTERS.value == 0 and (
                (ord("a") <= key <= ord("z")) or
                (ord("A") <= key <= ord("Z"))):
            self.text += chr(key)
            return

        if not acceptable_character & AcceptableCharacters.SPECIAL_CHARACTERS.NUMBERS.value == 0 and (
                (ord("0") <= key <= ord("9"))):
            self.text += chr(key)
            return

        if key == 127 and len(self.text) > 0:
            self.text = self.text[:-1]

    def render(self, y_position):
        height, width = self.__stdscr.getmaxyx()
        add_center_text(self.__stdscr, self.text, y_position, curses_colors["white_black"])
        if self.__active:
            self.__cursor.render(width // 2 + len(self.text) // 2 + (1 if len(self.text) % 2 == 1 else 0), y_position)

    def set_active(self, is_active: bool):
        self.__active = is_active
