import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.igdb.com/v4'
CLIENTID = os.environ['CLIENTID']
CLIENTSECRET = os.environ['CLIENTSECRET']

TARGET_ID = 14362

HEADERS = {
    'Client-ID': CLIENTID,
    'Authorization': 'Bearer ak08e61qy5cs1r4pmujvemqk5qt09s'
}

BASIC_FIELDS = f'fields name,release_dates,url,websites,artworks,cover; where id={TARGET_ID};'

basic_info = requests.post(f'{BASE_URL}/games', headers=HEADERS, data=BASIC_FIELDS).json()[0]

NAME = basic_info['name']
COVER_ID = basic_info['cover']
ARTWORKS_ID = basic_info['artworks']
RELEASE_DATES = basic_info['release_dates']
WEBSITES = basic_info['websites']

def fields_generator(fields: list[str]) -> str:
    """Generate fields"""
    return f'fields {",".join(fields)};'

def abstract_request(base_url: str, headers: dict[str, str]):
    """return a function which is applied with base_url and headers"""
    def endpoint_request(end_point: str, fields: list[str], id_array: int | list[int]):
        if isinstance(id_array, int):
            return requests.post(f'{base_url}/{end_point}', headers=headers, data=f'{fields_generator(fields)} where id={id_array};').json()[0]
        else:
            urls = [requests.post(f'{base_url}/{end_point}', headers=headers, data=f'{fields_generator(fields)} where id={id};').json()[0] for id in id_array]
            return urls
    return endpoint_request

base_request = abstract_request(BASE_URL, HEADERS)

class Card:
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

    release_dates = base_request('release_dates', ['human', 'platform'], RELEASE_DATES)
    # print(release_dates)

    websites = base_request('websites', ['url'], WEBSITES)
    websites_url = [element.get('url') for element in websites]
    # print(websites_url)

    the_last_of_us = Card(NAME, cover_url, artworks_url)
    print(f'Name: {the_last_of_us.name}')
    print(f'Cover: {the_last_of_us.cover}')
    print(f'Artworks: {the_last_of_us.artworks}')
