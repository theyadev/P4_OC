from menu import print_menu
from views.list_players import list_players_view
from controllers.play_next_turn import play_next_turn
from controllers.play_all_turns import play_all_turns

def tournament_actions_view(tournament):
    menu = [("List players", lambda: list_players_view(tournament.get_sorted_players(), sort_by="nothing", title="Leaderboard ---------")),
            # ("List matches", lambda: list_matches(tournament))
            ]

    if tournament.max_turns > tournament.current_round:
        menu.append(("Play next round", lambda tournament=tournament: play_next_turn(tournament)))
        menu.append(("Play all rounds", lambda tournament=tournament: play_all_turns(tournament)))

    menu.append(("Back", lambda: None))

    print_menu(menu)
