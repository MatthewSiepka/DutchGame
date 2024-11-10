import curses

curses_colors = {}

def init_color_scheme():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses_colors["cyan_black"] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses_colors["magenta_black"] = curses.color_pair(2)

    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses_colors["white_black"] = curses.color_pair(3)

    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses_colors["red_black"] = curses.color_pair(4)

    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses_colors["black_white"] = curses.color_pair(5)

