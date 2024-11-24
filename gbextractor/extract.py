import requests
from bs4 import BeautifulSoup


def get_soup(url, page=1):
    ''' Extract hmtl-presentation of search page'''

    response = requests.get(url+str(page))

    return BeautifulSoup(response.content, "html.parser")


def get_games_info(soup, language="English"):
    ''' Extract <a href=... class=...> elements of a page, 12 per page '''

    return soup.find_all(
        class_="btn btn-sm btn-secondary mb-1",
        title="In "+language
    )


def extract_game(game_info):
    ''' '''

    url = game_info.get("href")
    title = _extract_title(url)

    print("Extracted", title)
    return {
        "url": url,
        "title": title
    }


def _extract_title(url):
    ''' Extract title out of link'''

    title_full = url.split("/")[-1] \
                    .strip(".pdf")

    return " ".join(title_full.split("-")[1:-1])

def get_games(url,  language="English"):
    ''' Extracts title and download url of all games'''

    games_list = []

    for page in range(5): # substitute for dyn.solution
        print("Extracting from page", page)
        soup = get_soup(url, page)

        for game_info in get_games_info(soup, language=language):
            games_list.append(extract_game(game_info))

    return games_list
