import random
import names

from dataclasses import dataclass

from classes.Gender import Gender

from input import custom_input
from menu import print_menu
from data import read_json, write_json


@dataclass
class Player:
    _list = []

    id: int
    first_name: str
    last_name: str
    birth_date: str
    gender: Gender
    rating: int
    score: int = 0
    paired: bool = False

    @classmethod
    def new_from_input(self):
        first_name = custom_input("Enter first name: ")
        last_name = custom_input("Enter last name: ")
        birth_date = custom_input("Enter birth date: ")

        gender = print_menu([
            (gender.name, lambda: gender) for gender in Gender
        ])
        rating = ""
        while not rating.isdigit():
            rating = custom_input("Enter rating: ")

        rating = int(rating)

        for player in self._list:
            if player.first_name == first_name and player.last_name == last_name and player.birth_date == birth_date:
                return player

        player = Player.new(first_name, last_name, birth_date, gender, rating)

        return player

    @classmethod
    def get_by_id(self, id):
        for player in self._list:
            if player.id == id:
                return player
        return None

    @classmethod
    def random(self):
        first_name = names.get_first_name()
        last_name = names.get_last_name()

        birth_date = "/".join(
            [random.randint(1, 31).__str__(), random.randint(
                1, 12).__str__(), random.randint(1960, 2007).__str__()]
        )

        gender = random.choice([gender for gender in Gender])
        rating = random.randint(400, 1600)

        return Player.new(first_name, last_name, birth_date, gender, rating)

    @classmethod
    def new(self, *args):
        player = Player(random.randint(1, 100000000), *args)
        self._list.append(player)
        self.save()
        return player

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.rating})"

    def toJSON(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender.name,
            "rating": self.rating,
            "score": self.score,
        }

    @classmethod
    def load_json(self):
        self._list = []
        players_json = read_json('players.json')
        for player in players_json:
            self._list.append(Player(player['id'], player['first_name'], player['last_name'],
                              player['birth_date'], Gender[player['gender']], player['rating'], player['score']))

    @classmethod
    def save(self):
        write_json("players.json", [player.toJSON() for player in self._list])
