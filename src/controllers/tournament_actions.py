from views.tournament_actions import tournament_actions_view
from models.Tournament import Tournament

def tournament_actions(tournament_name: str):
    tournament = Tournament.find_by_name(tournament_name)
    if tournament is None:
        print("Tournament not found")
        return
    tournament_actions_view(tournament)