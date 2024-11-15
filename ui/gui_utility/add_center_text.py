def add_center_text(stdscr, text, y_position, color):
    height, width = stdscr.getmaxyx()
    stdscr.addstr(y_position, width // 2 - len(text) // 2, text, color)