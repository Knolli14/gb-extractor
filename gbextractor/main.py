
from gbextractor.params import URL
from gbextractor.extract import get_games
from gbextractor.data import save_games_list


if __name__ == "__main__":
    save_games_list(get_games(URL))
