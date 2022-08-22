from dataclasses import dataclass

from classes.Player import Player


@dataclass
class Match:
    players: tuple[Player, Player]
    is_draw: bool
    winner: int
