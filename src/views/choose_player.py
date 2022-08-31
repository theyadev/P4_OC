from menu import print_menu
from models.Player import Player
from controllers.create_player import create_player
from views.choose_player_from_list import choose_player_from_list_view


def choose_player_view(player_list):
    player = print_menu([
        ("Create new player", lambda: create_player()),
        ("Search player", lambda: choose_player_from_list_view(player_list)),
    ])

    return player
