"""View to list tournaments."""

from menu import print_menu
from controllers.tournament_actions import tournament_actions


def list_tournaments_view(tournament_list, page=0, per_page=8, sort_by=None):
    """List tournaments."""
    if sort_by is None:
        sort_by = print_menu([
            ("Sort by name", lambda: "name"),
            ("Sort by date", lambda: "date"),
        ])

    if sort_by == "name":
        tournament_list = sorted(tournament_list, key=lambda tournament: tournament.name, reverse=True)
    elif sort_by == "date":
        tournament_list = sorted(tournament_list, key=lambda tournament: tournament.start_date, reverse=True)

    tournaments = tournament_list[page * per_page: (page + 1) * per_page]
    has_previous = page > 0
    has_next = page < len(tournament_list) // per_page

    if len(tournaments) == 0:
        input("No tournaments found, press Enter to continue...")
        return None

    menu = []

    for tournament in tournaments:
        menu.append(
            (tournament.__str__(),
                lambda tournament=tournament: tournament_actions(tournament.name)))

    if has_next:
        menu.append(("Next page", lambda: list_tournaments_view(
            tournament_list, page=page + 1, sort_by=sort_by)))

    if has_previous:
        menu.append(
            ("Previous page", lambda: list_tournaments_view(tournament_list, page=page - 1, sort_by=sort_by)))

    menu.append(("Back", lambda: None))

    print_menu(menu)
