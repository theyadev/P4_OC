from classes.GameType import GameType
from classes.Match import Match
from models.Player import Player
from classes.Round import Round

from dataclasses import dataclass

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
    max_turns: int
    ended: bool

    @classmethod
=======
>>>>>>> mvc:src/models/Tournament.py
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
                    Round(turn['name'],
                          turn['start_date'],
                          turn['end_date'],
                          matchs))

            self._list.append(
                Tournament(tournament['name'],
                           tournament['location'],
                           tournament['start_date'],
                           tournament['end_date'],
                           rounds,
                           players,
                           GameType[tournament['game_type']],
                           tournament['description'],
                           tournament['current_round'],
                           tournament["max_turns"],
                           tournament['ended']))

    def get_player_score(self, player):
        score = 0
        for turn in self.turns:
            for match in turn.matchs:
                try:
                    if match.is_draw:
                        score += 0.5
                        continue

                    index = match.players.index(player)
                    if match.winner == index:
                        score += 1

                except ValueError:
                    continue

        return score

    def get_sorted_players(self):
        players = sorted(self.players, key=lambda x: x.rating, reverse=True)
        players = sorted(
            players, key=lambda x: self.get_player_score(x), reverse=True)

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

        self.save()

    def already_played_against(self, player1, player2):
        for turn in self.turns:
            for match in turn.matchs:
                player_ids = [player.id for player in match.players]
                if player1.id in player_ids and player2.id in player_ids:
                    return True
        return False

    def next_turn(self):
        if self.current_round == self.max_turns:
            self.ended = True
            return

        self.current_round += 1

        if len(self.turns) == 0:
            self.first_turn()
            return

        new_round = Round(len(self.turns) + 1,
                          self.start_date, self.end_date, [])

        players = self.get_sorted_players()

        for p in players:
            p.paired = False

        i = 0
        while i < len(players):
            if players[i].paired is False:
                k = i+1

                while players[k].paired:
                    k += 1
                while self.already_played_against(players[i], players[k]):
                    k += 1

                new_match = Match((players[i], players[k]))
                new_round.matchs.append(new_match)

                players[i].paired = True
                players[k].paired = True
            i += 1

        self.turns.append(new_round)

        self.save()

        return

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
            "max_turns": self.max_turns,
            "ended": self.ended
        }

    def __str__(self) -> str:
        return f"{self.name} - {self.location} - {self.start_date}"

    def play(self):
        while self.ended is False:
            self.next_turn()

            if self.ended is True:
                break
            self.turns[-1].set_scores()

    @classmethod
    def save(self):
        write_json('tournaments.json', [tournament.toJSON()
                   for tournament in self._list])
