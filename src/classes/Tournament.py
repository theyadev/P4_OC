from classes.GameType import GameType
from classes.Match import Match
from classes.Player import Player
from classes.Round import Round

from dataclasses import dataclass

from input import custom_input
from menu import print_menu
from data import read_json, write_json


@dataclass
class Tournament:
    _list = []

    name: str
    location: str
    start_date: str
    end_date: str
    turns: list[Round]
    players: list[Player]
    game_type: GameType
    description: str
    current_round: int
    ended: bool

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
            (game_type.name, lambda game_type=game_type: game_type) for game_type in GameType
        ], "Choose game type: ")

        description = custom_input("Enter description: ")

        tournament = Tournament(name, location, start_date, end_date,
                                turns, players, game_type, description, 0, False)

        self._list.append(tournament)

        self.save()

        return tournament

    @classmethod
    def load_json(self):
        self._list = []
        tournaments_json = read_json('tournaments.json')
        for tournament in tournaments_json:
            players = []
            rounds = []

            for player_id in tournament['players']:
                players.append(Player.get_by_id(player_id))

            for turn in tournament['turns']:
                matchs = []
                for match in turn['matchs']:
                    players = []
                    for player_id in match['players']:
                        players.append(Player.get_by_id(player_id))
                    matchs.append(Match(players))

                rounds.append(
                    Round(turn['name'], turn['start_date'], turn['end_date'], matchs))

            self._list.append(Tournament(tournament['name'], tournament['location'], tournament['start_date'], tournament['end_date'], rounds,
                              players, GameType[tournament['game_type']], tournament['description'], tournament['current_round'], tournament['ended']))
    
    def get_player_score(self, player):
        score = 0
        for turn in self.turns:
            for match in turn.matchs:
                try:
                    index = match.players.index(player)
                    if match.winner == index:
                        score += 1
                except ValueError:
                    continue
                
        return score

    def get_sorted_players(self):
        players = sorted(self.players, key=lambda x: x.rating, reverse=True)
        players = sorted(players, key=lambda x: self.get_player_score(x), reverse=True)

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

        while len(players) > 0:
            player1 = players.pop(0)
            player2 = players[0]

            if self.already_played_against(player1, player2) and len(players) > 1:
                player2 = players.pop(1)
            else:
                player2 = players.pop(0)

            new_match = Match((player1, player2))
            new_round.matchs.append(new_match)

        self.turns.append(new_round)

        self.current_round += 1

        self.save()

    def toJSON(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "turns": [turn.toJSON() for turn in self.turns],
            "players": [player.id for player in self.players],
            "game_type": self.game_type.name,
            "description": self.description,
            "current_round": self.current_round,
            "ended": self.ended
        }

    def __str__(self) -> str:
        return f"{self.name} - {self.location} - {self.start_date} - {self.end_date}"

    @classmethod
    def save(self):
        write_json('tournaments.json', [tournament.toJSON()
                   for tournament in self._list])
