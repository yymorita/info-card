"""
Provides config variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()

AUTH_URL = 'https://id.twitch.tv/oauth2/token'
BASE_URL = 'https://api.igdb.com/v4'
CLIENTID = os.environ['CLIENTID']
CLIENTSECRET = os.environ['CLIENTSECRET']
TOKEN = os.environ['TOKEN']
