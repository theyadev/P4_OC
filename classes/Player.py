from dataclasses import dataclass

from classes.Gender import Gender


@dataclass
class Player:
    first_name: str
    last_name: str
    birth_date: str
    gender: Gender
    rating: int
