import os
import json

from gbextractor.params import LOCAL_DATA_PATH

def save_games_list(games_list):
    ''' Saves the extracetd games_list locally'''

    games_dict = {"games": games_list}
    games_list_json = json.dumps(games_dict, indent=4)

    with open(os.path.join(LOCAL_DATA_PATH, "games_list.json"), "w") as output:
        output.write(games_list_json)

    print("File saved!")


def load_games_list():
    ''' Load the games_list dictionary '''

    with open(os.path.join(LOCAL_DATA_PATH, "games_list.json"), 'r') as file:
        data = json.load(file)

    print("Loaded 'games_list.json' !")
    return data

if __name__ == "__main__":

    print(load_games_list())
