"""View to select tournament actions."""

from menu import print_menu
from views.list_players import list_players_view
from controllers.play_next_turn import play_next_turn
from controllers.play_all_turns import play_all_turns
from controllers.list_rounds import list_rounds


def tournament_actions_view(tournament):
    """Select tournament actions."""
    menu = [
        ("List players", lambda: list_players_view(tournament.get_sorted_players(),
         sort_by="nothing", title="Leaderboard ---------")),
        ("List rounds", lambda: list_rounds(tournament))
    ]

    if tournament.max_turns > tournament.current_round:
        menu.append(("Play next round", lambda tournament=tournament: play_next_turn(tournament)))
        menu.append(("Play all rounds", lambda tournament=tournament: play_all_turns(tournament)))

    menu.append(("Back", lambda: False))

    return print_menu(menu, tournament)
