# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    START_TEXT = """text=START_TEXT.format(message.from_user.first_name)
"Hi {name},I am a anjumani footer bot join my channel https://t.me/anjumani_zone!

Don't use my bot or you will get ban !!
"""


 
