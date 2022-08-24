import random
import names

from dataclasses import dataclass

from classes.Gender import Gender

from input import custom_input
from menu import print_menu


@dataclass
class Player:
    first_name: str
    last_name: str
    birth_date: str
    gender: Gender
    rating: int
    score: int = 0

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

        return Player(first_name, last_name, birth_date, gender, rating)

    @classmethod
    def random(self):
        first_name = names.get_first_name()
        last_name = names.get_last_name()

        birth_date = "/".join(
            [random.randint(1, 31).__str__(), random.randint(1, 12).__str__(), random.randint(1960, 2007).__str__()]
        )

        gender = random.choice([gender for gender in Gender])
        rating = random.randint(400, 1600)

        return Player(first_name, last_name, birth_date, gender, rating)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.rating})"
