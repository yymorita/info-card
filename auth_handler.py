"""
Provides Authorizatoin functionality.
"""

import os
import requests
import constant as const

payload = {
    'client_id': const.CLIENTID,
    'client_secret': const.CLIENTSECRET,
    'grant_type': 'client_credentials',
}

HEADERS = {
    'Client-ID': const.CLIENTID,
    'Authorization': f'Bearer {const.TOKEN}'
}


class AuthHandler:
    """Manage authentication for API access."""

    def __init__(self, token):
        self.__token = token

    @property
    def token(self):
        """token property."""

    @token.getter
    def token(self):
        """token getter."""
        return self.__token

    def check_token(self) -> bool:
        """
        Check if the current token is valid.
        Returns True if the token is valid.
        """
        is_valid = False
        http_status = requests.post(
            f'{const.BASE_URL}/games', headers=HEADERS, data='fields name;').status_code
        if http_status == 200:
            is_valid = not is_valid
        return is_valid

    def generate_token(self):
        """return bearer token. and set as environmental variable"""
        token = requests.post(const.AUTH_URL, params=payload).json()
        os.environ['TOKEN'] = token
        return token


if __name__ == '__main__':
    current_token = const.TOKEN
    manager = AuthHandler(current_token)
    is_token_valid = manager.check_token()
    if not is_token_valid:
        manager.generate_token()
    print(f'Bearer token: {manager.token}')
