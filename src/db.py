import os
from tinydb import TinyDB

if not os.path.exists("./data"):
    os.mkdir("./data")
players_db = TinyDB('./data/players.json')
tournaments_db = TinyDB('./data/tournaments.json')
