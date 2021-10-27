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
    APP_ID = int(os.environ.get("APP_ID", "3596842"))
    API_HASH = os.environ.get("API_HASH", "d8f83c77dd83a3f4b8d64da78ddebe1a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2089774427:AAGIyfdvaqF7NCk0nrnVJOIpGLSqD5qLSSM")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1581771541 829696828").split())
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "-1001496561987").split())
    USER_SESSION = os.environ.get("USER_SESSION", "BQBWKVw9MurhpjQTswYAFvbTTK1XNHSDbHHidbooUSD3I9sq7CekR3_lNuZrzWUrVcG5V3nx1E-85nl_183PPs8CK3RyoNhLu9XwNXj8qtjqt4rG5Gt8gQWIvhO9lpUZMx7nBD_31fwvKGaA0nQB1tRFfXbed7IBqDWNvfZTpToiq8YCoE2w9ftlFinW-RLIzESlIkGNtMeI5ekRuDjErEVIvAL526QFMt0ScJ-Ac8Wu0Bxeh5bYl7lX30nOoLz9ZggK-zc0ggoYsbTO9d-0YSt7uIdSDN3ekFBM0PC8txDkbd6Qi3RV2Msm7RjoQHelh9M97yI0gGX-OLXsKSTgkVe2XxF-8AA")
    BOTTOM_CAPTION = os.environ.get("BOTTOM_CAPTION", False)
    ENV = os.environ.get("ENV", "ANYTHING")
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
