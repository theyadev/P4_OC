from dataclasses import dataclass

from classes.Match import Match


@dataclass
class Round:
    name: str
    start_date: str
    end_date: str
    matchs: list[Match]
