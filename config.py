import logging
from telethon import TelegramClient
from os import getenv
from dotenv import load_dotenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

TOKEN = getenv("TOKEN", default=None)
