from classes.Match import Match
from classes.Round import Round
from classes.Tournament import Tournament
from classes.Player import Player
from classes.GameType import GameType
from classes.Gender import Gender

from datetime import datetime


if __name__ == "__main__":
    player = Player.random()
    print(player)
    # p = Player.new_from_input()
    p = Tournament.new_from_input()
    last_round = None
    while last_round != False:
        last_round = p.next_turn()
        p.turns[0].set_scores()
    
    for turn in p.turns:
        for match in turn.matchs:
            print(match)