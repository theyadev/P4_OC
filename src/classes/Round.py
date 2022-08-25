from classes.Match import Match

from dataclasses import dataclass

from menu import print_menu


@dataclass
class Round:
    name: str
    start_date: str
    end_date: str
    matchs: list[Match]

    def set_scores(self):
        while True:
            menu = []
            [menu.append((match.__str__(), lambda i=i: i))
             for i, match in enumerate(self.matchs)]

            menu.append(("Next", lambda: False))

            res = print_menu(menu, f"Choose winners of round {self.name} : ")

            if res is False:
                break

            self.matchs[res].set_score()

    def __str__(self):
        return f"Round \"{self.name}\": {len(self.matchs)} matchs"

    def toJSON(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matchs": [match.toJSON() for match in self.matchs]
        }
