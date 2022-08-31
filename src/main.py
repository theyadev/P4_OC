from models.Tournament import Tournament
from models.Player import Player
from time import sleep

from views.index import index_view



def main():
    Player.load_json()
    Tournament.load_json()

    while True:
        index_view()
        sleep(1)


if __name__ == "__main__":
    main()

    p = Tournament.new_from_input()

    # for turn in p.turns:
    #     for match in turn.matchs:
    #         print(match)

    sorted_players = p.get_sorted_players()
    for player in sorted_players:
        score = p.get_player_score(player)
        print(f"{player.__str__()} : {score}")
