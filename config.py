import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "20892978"
API_HASH = "ab1bf6b3740eedc41db3bd1a390e54e0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7825465869:AAH8-7Y9LWtA9PWCI119FaZehYmTQytr-4I"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb://Projectxxx:lodekadbworkbckundkiyrahkrgamadarchod@madarchod-shard-00-00.zgzrc.mongodb.net:27017,madarchod-shard-00-01.zgzrc.mongodb.net:27017,madarchod-shard-00-02.zgzrc.mongodb.net:27017/test?ssl=true&replicaSet=atlas-123-shard-0&authSource=admin&retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

# Chat id of a group for logging bot's activities
LOGGER_ID = "-1002424715795"

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "5458968679"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SquirtleRivals09/ErenMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Senoritabot_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Senoritabot_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQE-zTIABr934rQKB_ekWzBmFyenHi1E9GcKiV7Y6MdgnsAvC-XPaGA2AeQo2OR9UTrC0f8BTHoapZ68fycynvY52VFaJs3gEtjF31rrPKJLVoht8PXV8UPFOko1TiFghZDk56IO2oH_T4lxpBS9fW40d14se9M9vSWl5pbsdUDcJs7T9t8X-oh3oStU8fYW5s6sYh4tnjxZQpRt4ssRkrx7iICDOw00dt3-5z41jjW1D81nwIVDDbIE1_X2ZCej3MIQFdrrmtw-PbhusYJVDUvheX2TWHola9YQYvw2g4Zbau0-GzcWVZWL0Nta-vF8SRBzii0goi8wwaZJW8yFcusH3f3qUgAAAAHPEKwBAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/01ba8cd4c05f3f83af28c-f8afa1b0676f1fa92c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/4fdaf06331c40028651c9-d78d4bd2b7dfcae80e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/b62173af4bca080eb2556-4e535d45b195bba255.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
STREAM_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
