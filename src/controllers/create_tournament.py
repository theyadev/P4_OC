from classes.Tournament import Tournament
from views.choose_player import choose_player_view
from views.create_tournament import create_tournament_view

from time import sleep


def create_tournament():
    tournament = create_tournament_view()

    while len(tournament.players) < 8:
        player = choose_player_view()

        if player is None:
            continue

        if player.id in [player.id for player in tournament.players]:
            print("Player already in the tournament")
            sleep(1)
            continue

        tournament.players.append(player)

    Tournament._list.append(tournament)

    Tournament.save()
