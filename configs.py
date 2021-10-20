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
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "@OB_LINKS")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "").split())
    USER_SESSION = os.environ.get("USER_SESSION", "")
    BOTTOM_CAPTION = os.environ.get("BOTTOM_CAPTION", False)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    START_TEXT = """
I am a Different type Auto Filter Bot.

Click /Help Button For More🙊. 

Made by @OwDvEr_BoT 🔥
    """
    HELP_TEXT = """
<b><i><u>How To Use Me!?</u></i></b>
<i>
-> Just Go To My Movie Group And Ask For A Movie (Example: "Luca 2019" or "Luca")
</i>
<b><i><u>How To Add Me To Your Group!?</u></i></b>
<i>
-> Click /start
-> Click The "➕ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕" Button
-> Then Choose The Group Which You Need To Add Me  
-> Then Make Me Admin
</i>


@OwDvEr_BoT
"""


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
