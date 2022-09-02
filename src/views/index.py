from controllers.list_tournaments import list_tournaments
from controllers.list_players import list_players
from controllers.create_tournament import create_tournament
from controllers.create_player import create_player
from menu import print_menu


def index_view():
    print_menu([
        ("Create new player", lambda: create_player()),
        ("List players", lambda: list_players()),
        ("List tournaments", lambda: list_tournaments()),
        ("Create new tournament", lambda: create_tournament()),
        # ("Search tournament", lambda: Tournament.from_list()),
        ("Exit program", lambda: exit()),
    ])
