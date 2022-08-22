from classes.Match import Match
from classes.Round import Round
from classes.Tournament import Tournament
from classes.Player import Player
from classes.GameType import GameType
from classes.Gender import Gender

from datetime import datetime

def custom_input(string: str):
    res = None
    while not res or res == "":
        res = input(string)

    return res

def create_player():
    first_name = custom_input("Enter first name: ")
    last_name = custom_input("Enter last name: ")
    birth_date = custom_input("Enter birth date: ")

    gender = None

    while gender != "M" and gender != "F":
        gender = custom_input("Enter Gender (M/F): ").upper()

    rating = ""
    while not rating.isdigit():
        rating = custom_input("Enter rating: ")

    rating = int(rating)

    return Player(first_name, last_name, birth_date, gender, rating)



if __name__ == "__main__":
    p = create_player()
    print(vars(p))