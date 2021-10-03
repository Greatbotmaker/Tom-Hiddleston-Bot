# (c) @Owdver

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "").split())
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", False)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    START_TEXT = """
I am a Different type Auto Filter Bot.

Click Help Button For More🙊. 

Made by @OwDvEr_BoT 🔥
    """


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
