from menu import print_menu
from classes.Player import Player


def choose_player_view():
    player = print_menu([
        ("Create new player", lambda: Player.new_from_input()),
        ("Create random player", lambda: Player.random()),
        ("Search player", lambda: Player.from_list()),
    ])

    return player
