import json
import os

BASE_PATH = "data/"


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass


def read_json(file_name):
    try:
        with open(BASE_PATH + file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError or json.decoder.JSONDecodeError:
        return []


def write_json(file_name, data):
    create_folder(BASE_PATH)

    with open(BASE_PATH + file_name, 'w') as f:
        json.dump(data, f)
