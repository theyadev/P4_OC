"""View to list players."""

from utils.menu import print_menu


def list_players_view(player_list, page=0, per_page=8, sort_by=None, title="Players"):
    """List players."""
    if sort_by is None:
        sort_by = print_menu([
            ("Sort by rating", lambda: "rating"),
            ("Sort by first name", lambda: "first_name"),
            ("Sort by last name", lambda: "last_name"),
        ])

    if sort_by == "rating":
        player_list = sorted(
            player_list, key=lambda player: player.rating, reverse=True)
    elif sort_by == "first_name":
        player_list = sorted(player_list, key=lambda player: player.first_name)
    elif sort_by == "last_name":
        player_list = sorted(player_list, key=lambda player: player.last_name)

    players = player_list[page * per_page: (page + 1) * per_page]
    has_previous = page > 0
    has_next = page < (len(player_list) // per_page) - 1
    if len(players) == 0:
        input("No players found, press Enter to continue...")
        return None

    menu = []

    for player in players:
        menu.append(
            (player.__str__(),
                lambda player=player: print(player.__str__())))

    if has_next:
        menu.append(("Next page", lambda: list_players_view(
            player_list, page=page + 1, sort_by=sort_by)))

    if has_previous:
        menu.append(
            ("Previous page", lambda: list_players_view(player_list, page=page - 1, sort_by=sort_by)))

    menu.append(("Back", lambda: None))

    print_menu(menu, title)
