import curses

from dutch_core.card.card import Card, CardsRank


def render_card(stdr: curses.window, y: int, x: int, card: Card | None, color):
    window = curses.newwin(4, 6, y, x)
    window.addstr(0, 0, "_____", color)
    window.addstr(1, 0, "|///|", color)
    window.addstr(2, 0, "|///|", color)
    window.addstr(3, 0, "-----", color)

    if card is not None:
        card_color = curses.color_pair(4) if card.card_color.value["color"] == "red" else curses.color_pair(3)
        icon = card.card_color.value["icon"]
        window.addstr(1, 1, f"{icon}  ", card_color)
        window.addstr(1, 5, f"|", color)
        window.addstr(2, 1, f"{card.card_rank.value}{" " if card.card_rank == CardsRank.TEN else "  "}", color)
    window.overlay(stdr)
    window.refresh()
