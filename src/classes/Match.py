from dataclasses import dataclass

from models.Player import Player
from menu import print_menu


@dataclass
class Match:
    players: tuple[Player, Player]
    is_draw: bool = False
    winner: int = None

    def set_score(self):
        result = print_menu([
            (self.players[0].__str__(), lambda: 0),
            (self.players[1].__str__(), lambda: 1),
            ("Draw", lambda: 2),
        ], "Choose winner: ")

        if result == 2:
            self.is_draw = True

            return

        self.winner = result

    def __str__(self):
        return f"{self.players[0]} vs {self.players[1]} {'(DRAW)' if self.is_draw else f'(WINNER: {self.players[self.winner]})' if self.winner is not None else ''}"

    def toJSON(self):
        return {
            "players": [player.id for player in self.players],
            "is_draw": self.is_draw,
            "winner": self.winner
        }
