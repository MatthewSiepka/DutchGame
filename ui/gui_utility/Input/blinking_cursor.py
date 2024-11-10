import curses
import time

from ui.gui_utility.color_scheme import curses_colors


class BlinkingCursor:
    __stdscr: curses.window
    __last_blink_time: float
    __blinking_speed = 0.5
    __is_blinking: bool

    def __init__(self, stdscr: curses.window):
        self.__stdscr = stdscr
        self.__is_blinking = False
        self.__last_blink_time = time.time()

    def __updateBlink(self):
        new_time = time.time()
        if(new_time - self.__last_blink_time < self.__blinking_speed):
            return
        self.__is_blinking = not self.__is_blinking
        self.__last_blink_time = new_time


    def render(self, x_position, y_position):
        self.__updateBlink()
        color = curses_colors["black_white"] if not self.__is_blinking else curses_colors["white_black"]
        self.__stdscr.addstr(y_position, x_position, " ", color)



