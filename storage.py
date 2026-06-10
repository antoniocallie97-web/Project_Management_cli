import json
import os

FILE_NAME = "data.json"


def save_data(users):
    data = [user.to_dict() for user in users]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)