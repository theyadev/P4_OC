from classes.Match import Match
from classes.Round import Round
from classes.Tournament import Tournament
from classes.Player import Player
from classes.GameType import GameType
from classes.Gender import Gender

from datetime import datetime


if __name__ == "__main__":
    # p = Player.new_from_input()
    Player.load_json()
    Tournament.load_json()

    p = Tournament.new_from_input()

    while p.current_round < 3:
        p.next_turn()
        p.turns[-1].set_scores()

    # for turn in p.turns:
    #     for match in turn.matchs:
    #         print(match)
    
    sorted_players = p.get_sorted_players()
    for player in sorted_players:
        score = p.get_player_score(player)
        print(f"{player.__str__()} : {score}")
