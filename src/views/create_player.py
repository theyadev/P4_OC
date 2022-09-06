"""View to create a player."""

from models.Gender import Gender
from utils.input import custom_input
from utils.menu import print_menu


def create_player_view():
    """Create a player."""
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

    return (first_name, last_name, birth_date, gender, rating)
