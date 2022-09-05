"""Controller to render the tournament actions view."""

from views.tournament_actions import tournament_actions_view
from models.Tournament import Tournament


def tournament_actions(tournament_name: str):
    """Tournament actions."""
    tournament = Tournament.find_by_name(tournament_name)
    if tournament is None:
        print("Tournament not found")
        return
    ret = None

    for player in tournament.players:
        player.score = tournament.get_player_score(player)

    while ret is not False:
        ret = tournament_actions_view(tournament)

    for player in tournament.players:
        player.score = 0
