"""
Create Card Object.
"""

import requests
import auth_handler
import constant as const
import abstract_request

TARGET_ID = 14362

HEADERS = {
    'Client-ID': const.CLIENTID,
    'Authorization': f'Bearer {const.TOKEN}'
}

BASIC_FIELDS = f'fields name,release_dates,url,websites,artworks,cover; where id={TARGET_ID};'

basic_info = requests.post(
    f'{const.BASE_URL}/games', headers=HEADERS, data=BASIC_FIELDS).json()[0]

NAME = basic_info['name']
COVER_ID = basic_info['cover']
ARTWORKS_ID = basic_info['artworks']
RELEASE_DATES = basic_info['release_dates']
WEBSITES = basic_info['websites']

base_request = abstract_request.abstract_request(const.BASE_URL, HEADERS)


class Card:
    """Basic game informaiton"""
    name: str
    cover: str
    artworks: list[str]

    def __init__(self, name, cover, artworks):
        self.name = name
        self.cover = cover
        self.artworks = artworks


if __name__ == '__main__':
    artworks = base_request('artworks', ['url'], ARTWORKS_ID)
    artworks_url = [element.get('url') for element in artworks]
    # print(artworks_url)

    cover = base_request('covers', ['url'], COVER_ID)
    cover_url = cover['url']
    # print(cover_url)

    release_dates = base_request(
        'release_dates', ['human', 'platform'], RELEASE_DATES)
    # print(release_dates)

    websites = base_request('websites', ['url'], WEBSITES)
    websites_url = [element.get('url') for element in websites]
    # print(websites_url)

    this_game = Card(NAME, cover_url, artworks_url)
    print(f'Name: {this_game.name}')
    print(f'Cover: {this_game.cover}')
    print(f'Artworks: {this_game.artworks}')
