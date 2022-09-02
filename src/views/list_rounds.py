from menu import print_menu
from controllers.list_matches import list_matches

def list_rounds_view(turns):
    menu = [
        (f"Turn {turn.name}", lambda turn=turn: list_matches(turn)) for turn in turns
    ]
    menu.append(("Back", lambda: None))

    print_menu(menu, title="Rounds ---------")
