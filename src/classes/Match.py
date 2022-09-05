"""Class for a match."""

from dataclasses import dataclass

from models.Player import Player
from menu import print_menu


@dataclass
class Match:
    """Class for a match."""

    players: tuple[Player, Player]
    is_draw: bool = False
    winner: int = None

    def set_score(self):
        """Ask the user to set the winner of the match."""
        result = print_menu([
            (self.players[0].__str__(), lambda: 0),
            (self.players[1].__str__(), lambda: 1),
            ("Draw", lambda: 2),
        ], "Choose winner: ")

        if result == 2:
            self.is_draw = True

            return

        self.winner = result

    def toJSON(self):
        """Return a JSON representation of the match."""
        return {
            "players": [player.id for player in self.players],
            "is_draw": self.is_draw,
            "winner": self.winner
        }

    def __str__(self):
        """Return a string representation of the match."""
        if self.is_draw:
            x = "(Draw)"
        elif self.winner is not None:
            x = f"(Winner: {self.players[self.winner].first_name})"
        else:
            x = ""

        return f"{self.players[0]} vs {self.players[1]} {x}"
