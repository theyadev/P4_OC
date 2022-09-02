from menu import print_menu


def list_matches_view(matchs):
    menu = [
        (match.__str__(), lambda match=match: None) for match in matchs
    ]
    menu.append(("Back", lambda: None))

    print_menu(menu, title="Matches ---------")