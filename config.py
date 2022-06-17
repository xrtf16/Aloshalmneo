## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBSE2kDr9qBp22TGs5OfKqLLutWBAEee2ycPWnkEHDPyUGWFhe7iso3-3nFsSvY-63NGZy8Hz_zpv_I0NLvagGAjc-IRitmx8hTxEuL07XlHZ2R2joeQb0ambyTkIOm--MfoavdP8qyxafaeyWO2Yk6mTqUzCgwKCGgHTC1nbhUuPjuY_aSYiesiJSxgWjxHWIbA1HgjxkPlnlpYjylDjQjWNJS5t7gReoVCtEA5JXjEE6ocR7YBZgp4UfN-v34MopI_SZjJog2z4ZVc9CyoP8Sgt8opDjVkB5Rlx5RIA7eP19GQU2i2Xo7dnBBQg9q1YbdXx86ohHWJxH7n-1lP00iAAAAAS-lV8wA")
BOT_TOKEN = getenv("BOT_TOKEN", "5459233092:AAHSf0xnEEpWagetjUUgBUU_d4MwOaOcxi8")
BOT_NAME = getenv("BOT_NAME", "B𝑂𝑇 AL𝑂𝑆𝐻 𝑀𝐔𝑆𝐼𝐶 𓌹♱𓌺")
API_ID = int(getenv("API_ID", "9513898"))
API_HASH = getenv("API_HASH", "56a4b854278cc1adee7bd37ed1deb314")
OWNER_NAME = getenv("OWNER_NAME", "ali𓌹♱𓌺")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ghost022")
ALIVE_NAME = getenv("ALIVE_NAME", "xlx")
BOT_USERNAME = getenv("BOT_USERNAME", "alosh69_bot")
OWNER_ID = getenv("OWNER_ID", "655238474")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "mus_sic69")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QII_ll")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QII_ll")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "655238474").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES",").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
