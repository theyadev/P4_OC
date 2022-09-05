from models.Tournament import Tournament
from models.Player import Player

from views.index import index_view


def main():
    Player.load_json()
    Tournament.load_json()

    while True:
        index_view()


if __name__ == "__main__":
    main()
