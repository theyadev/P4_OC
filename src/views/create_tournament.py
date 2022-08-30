from classes.Tournament import Tournament
from classes.GameType import GameType
from input import custom_input
from menu import print_menu


def create_tournament_view():
    name = custom_input("Enter name: ")
    location = custom_input("Enter location: ")
    start_date = custom_input("Enter start date: ")
    end_date = custom_input("Enter end date: ")
    max_turns = 4
    turns = []
    players = []

    game_type = print_menu([
        (game_type.name, lambda game_type=game_type: game_type) for game_type in GameType
    ], "Choose game type: ")

    description = custom_input("Enter description: ")

    tournament = Tournament(name, location, start_date, end_date,
                            turns, players, game_type, description, 0, max_turns, False)

    return tournament
