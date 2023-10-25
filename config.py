import os
from dotenv import load_dotenv

from exceptions import BotTokenNotFoundException

load_dotenv()

TOKEN = os.environ.get('TOKEN')

if not TOKEN:
    raise BotTokenNotFoundException()
