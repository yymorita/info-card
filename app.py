"""
Create Card Object.
"""

import auth_handler
import constant as const
import abstract_request
import md_card

TARGET_ID = 14362

HEADERS = {
    'Client-ID': const.CLIENTID,
    'Authorization': f'Bearer {const.TOKEN}'
}

BASIC_FIELDS = ['name', 'release_dates',
                'url', 'websites', 'artworks', 'cover']


if __name__ == '__main__':
    auth_manager = auth_handler.AuthHandler(const.TOKEN)
    if not auth_manager.check_token():
        auth_manager.update_token()

    base_request = abstract_request.abstract_request(const.BASE_URL, HEADERS)
    basic_info = base_request('games', BASIC_FIELDS, TARGET_ID)

    TITLE = basic_info['name']
    COVER_ID = basic_info['cover']
    ARTWORKS_ID = basic_info['artworks']
    RELEASE_DATES = basic_info['release_dates']
    WEBSITES = basic_info['websites']

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

    this_game = md_card.Card(TITLE, cover_url, artworks_url)
    print(f'Title: {this_game.name}')
    print(f'Cover: {this_game.cover}')
    print(f'Artworks: {this_game.artworks}')
