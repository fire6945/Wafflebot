import os

import dotenv

from bot.bot import Wafflebot

dotenv.load_dotenv()
token = os.getenv("TOKEN")
bot = Wafflebot(token)
bot.run()