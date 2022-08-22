from dataclasses import dataclass
from classes.GameType import GameType

from classes.Player import Player


@dataclass
class Tournament:
    name: str
    location: str
    start_date: str
    end_date: str
    turns: str
    players: list[Player]
    game_type: GameType
    description: str
