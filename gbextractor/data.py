import os
import json

from gbextractor.params import LOCAL_DATA_PATH

def save_games_list(games_list):
    ''' Saves the extracetd games_list locally'''

    games_dict = {"games": games_list}
    games_list_json = json.dumps(games_dict, indent=4)

    save_path = os.path.join(LOCAL_DATA_PATH, "games_list.json")
    with open(save_path, "w") as output:
        output.write(games_list_json)

    print("Dict of all games saved locally:", save_path)


def load_games_list():
    ''' Load the games_list dictionary '''

    with open(os.path.join(LOCAL_DATA_PATH, "games_list.json"), 'r') as file:
        data = json.load(file)

    print("Loaded 'games_list.json' !")
    return data

def save_pdf(content, title):
    ''' Save PDF of a boardgame'''

    filename = os.path.join(LOCAL_DATA_PATH, "pdfs", title+".pdf")

    with open(filename, "wb") as f:
        f.write(content)
