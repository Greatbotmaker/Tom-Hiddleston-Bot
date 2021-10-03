# (c) @Owdver

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "").split())
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", False)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    START_TEXT = """
I am a different type auto filter bot.

ask a movie in my group.

Made by @OwDvEr_BoT
    """


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
