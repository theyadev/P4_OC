"""View to create or choose a player."""

from utils.menu import print_menu

from controllers.create_player import create_player
from views.choose_player_from_list import choose_player_from_list_view


def choose_player_view(player_list):
    """Choose an action, create or search."""
    player = print_menu([
        ("Create new player", lambda: create_player()),
        ("Search player", lambda: choose_player_from_list_view(player_list)),
    ])

    return player
