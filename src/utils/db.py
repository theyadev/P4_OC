"""Database interface for the application."""

import os
from tinydb import TinyDB

PATH = "./data"

if not os.path.exists(PATH):
    os.mkdir(PATH)

players_db = TinyDB(PATH + '/players.json')
tournaments_db = TinyDB(PATH + '/tournaments.json')
