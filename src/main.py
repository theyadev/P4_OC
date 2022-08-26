from classes.Match import Match
from classes.Round import Round
from classes.Tournament import Tournament
from classes.Player import Player
from classes.GameType import GameType
from classes.Gender import Gender

from datetime import datetime

from menu import print_menu

from time import sleep

def main():
    Player.load_json()
    Tournament.load_json()

    while True:
        action = print_menu([
            ("Create new player", lambda: Player.new_from_input()),
            ("List players", lambda: Player.list()),
            # ("List tournaments", lambda: Tournament.list()),
            ("Create new tournament", lambda: Tournament.new_from_input()),
            # ("Search tournament", lambda: Tournament.from_list()),
        ])

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
