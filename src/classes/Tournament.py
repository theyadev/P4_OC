from classes.GameType import GameType
from classes.Match import Match
from classes.Player import Player
from classes.Round import Round

from dataclasses import dataclass

from input import custom_input
from menu import print_menu

import time


@dataclass
class Tournament:
    name: str
    location: str
    start_date: str
    end_date: str
    turns: list[Round]
    players: list[Player]
    game_type: GameType
    description: str

    @classmethod
    def new_from_input(self):
        name = custom_input("Enter name: ")
        location = custom_input("Enter location: ")
        start_date = custom_input("Enter start date: ")
        end_date = custom_input("Enter end date: ")
        turns = []
        players = []

        for i in range(8):
            # player = print_menu([
            #     ("Create new player", lambda: Player.new_from_input()),
            #     ("Create random player", lambda: Player.random()),
            #     ("Search player", lambda: None),
            # ])
            player = Player.random()
            players.append(player)

        game_type = print_menu([
            (game_type.name, lambda: game_type) for game_type in GameType
        ], "Choose game type: ")

        description = custom_input("Enter description: ")

        return Tournament(name, location, start_date, end_date, turns, players, game_type, description)

    def get_sorted_players(self):
        players = sorted(self.players, key=lambda x: x.rating, reverse=True)
        players = sorted(players, key=lambda x: x.score, reverse=True)

        return players

    def first_turn(self):
        players = self.get_sorted_players()

        first_group = players[:len(players) // 2]
        second_group = players[len(players) // 2:]

        x = list(zip(first_group, second_group))

        new_round = Round(len(self.turns) + 1,
                          self.start_date, self.end_date, [])

        for i in x:
            new_match = Match((i[0], i[1]))
            new_round.matchs.append(new_match)

        self.turns.append(new_round)

    def already_played_against(self, player1, player2):
        for turn in self.turns:
            for match in turn.matchs:
                players_str = [player.__str__() for player in match.players]
                if player1.__str__() in players_str and player2.__str__() in players_str:
                    return True
        return False

    def next_turn(self):
        if len(self.turns) == 0:
            self.first_turn()
            return

        players = self.get_sorted_players()

        new_round = Round(len(self.turns) + 1,
                          self.start_date, self.end_date, [])

        for player in players:
            for player2 in players:
                if player == player2:
                    continue

                if self.already_played_against(player, player2):
                    continue
                new_match = Match((player, player2))
                new_round.matchs.append(new_match)
                break

        if len(new_round.matchs) == 0:
            return False

        self.turns.append(new_round)

    def __str__(self) -> str:
        return f"{self.name} - {self.location} - {self.start_date} - {self.end_date}"