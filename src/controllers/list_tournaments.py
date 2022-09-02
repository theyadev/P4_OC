from views.list_tournaments import list_tournaments_view
from models.Tournament import Tournament


def list_tournaments():
    list_tournaments_view(Tournament._list)
