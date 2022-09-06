"""Player class."""

import random
import names

from dataclasses import dataclass

from models.Gender import Gender
from utils.db import players_db
from tinydb import Query

PER_PAGE = 10


@dataclass
class Player:
    """Player class."""

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
    def load_json(self):
        """Load players from db."""
        self._list = []
        players_json = players_db.all()
        for player in players_json:
            self._list.append(
                Player(player['id'],
                       player['first_name'],
                       player['last_name'],
                       player['birth_date'],
                       Gender[player['gender']],
                       player['rating'],
                       player['score']
                       ))

    @classmethod
    def get_player_if_exists(cls, first_name, last_name, birth_date):
        """Return a player if exists."""
        for player in cls._list:
            if (player.first_name == first_name and
                    player.last_name == last_name and
                    player.birth_date == birth_date):
                return player

        return None

    @classmethod
    def get_by_id(self, id):
        """Return a player by id."""
        for player in self._list:
            if player.id == id:
                return player
        return None

    @classmethod
    def random(self):
        """Return a random player."""
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
        """Create a new player."""
        player = Player(random.randint(1, 100000000), *args)
        self._list.append(player)
        player.save()
        return player

    def toJSON(self):
        """Return a JSON representation of the player."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender.name,
            "rating": self.rating,
            "score": self.score,
        }

    def save(self):
        """Save the player in db."""
        player = Query()
        players_db.upsert(self.toJSON(), player.id == self.id)

    def __str__(self):
        """Return a string representation of the player."""
        return f"{self.first_name} {self.last_name} ({self.rating}) {self.score if self.score > 0 else ''}"
