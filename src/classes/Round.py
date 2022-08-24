from dataclasses import dataclass

from classes.Match import Match


@dataclass
class Round:
    name: str
    start_date: str
    end_date: str
    matchs: list[Match]

    def set_scores(self):
        for match in self.matchs:
            match.set_score()

    def __str__(self):
        return f"Round \"{self.name}\": {len(self.matchs)} matchs"