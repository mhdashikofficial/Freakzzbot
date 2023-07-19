import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('6363103413:AAFJ6KCv9l2llr9UigP5SR-plWsN7RhzJUY')
API_ID = int(os.environ.get('24323145'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQFzJEkAa_3KKeD2vQrYkgk5uaPud-xB9AjjV2LnUO_bG3ncBlnjk5yFkBFsEzNwE5liS5IDISBasaeZT_2LjZqpSESUFZCvUgZzxCkDwHaZhA2yaWpGNAnpDBr9IvmfjfAVmF46ROJXp_FXLjeTsRGkqVoW66dblmF6JYyM_5YRsJ35MMIG-ZeE1-ZbRPXr43ZAPyReTSfOg7m8t-GgGhpIkXbid3TogfKXSFqaeyTKeQVvaNDrKNR9hsSVpmbBBXqQaypqRESDiEeAMaWC1jOUWGcmiGlL79kpGespvkCG5PRf2Gc8Zgcu5dOZGyy3fnb2mDl3_koJ_u1YHqPkV-05-MypKgAAAABS70r0AA')
API_HASH = os.environ.get('2255461d65e3ad2440a936bc078b301f')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('+917356620538')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '1391414004').split()))
LOG_GROUP_ID = int(os.environ.get('-1001969201634'))
GBAN_LOG_GROUP_ID = int(os.environ.get('-1001969201634'))
MESSAGE_DUMP_CHAT = int(os.environ.get('-1001969201634'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
