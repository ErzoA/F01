# (©)Codexbotz
# Recife By sanyagesya
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5687211483:AAHb1gFS2Za7zV8TV0A-LTwsvWxgld1Ky5I")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "8529843"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e06fb8f7b42fb33821f272597321bc1")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001691579646"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2133434438"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "saya_wiki")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://kevskyux:AR4OqVZ5AvaDJdCvHtIkjEMVhTuz6CQT@suleiman.db.elephantsql.com/kevskyux")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "chnlwiki")
GROUP = os.environ.get("GROUP", "AboutWiki")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001525776016"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001508910413"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001869722299"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1001865354149"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Yoo {first}</b>\n\n<b>Saya bot asupan.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "2133434438").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Yoo {first}\n\nJoin dulu yang di bawah baru ada videony</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(2133434438)
ADMINS.append(1980553307)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
