from models.Tournament import Tournament
from models.Player import Player
from time import sleep

from views.index import index_view


def main():
    Player.load_json()
    Tournament.load_json()

    while True:
        index_view()


if __name__ == "__main__":
    main()

    p = Tournament.new_from_input()

    # for turn in p.turns:
    #     for match in turn.matchs:
    #         print(match)
