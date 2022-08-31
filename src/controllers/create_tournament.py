from models.Tournament import Tournament
from models.Player import Player

from views.choose_player import choose_player_view
from views.create_tournament import create_tournament_view

from time import sleep


def create_tournament():
    tournament_data = create_tournament_view()

    tournament = Tournament(*tournament_data)

    while len(tournament.players) < 8:
        player_data = choose_player_view(Player._list)

        if type(player_data) == Player:
            player = player_data
        elif type(player_data) == tuple:
            player = Player.get_player_if_exists(
                player_data[0], player_data[1], player_data[2])

            if player is None:
                player = Player.new(*player_data)
        else:
            continue

        if player.id in [player.id for player in tournament.players]:
            print("Player already in the tournament")
            sleep(1)
            continue

        tournament.players.append(player)

    Tournament._list.append(tournament)

    Tournament.save()

    return tournament
