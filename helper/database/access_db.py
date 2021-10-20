# (c) @AbirHasan2005

from configs import Config
from helper.database.database import Database

db = Database(Config.MONGODB_URI, Config.USER_SESSION)
