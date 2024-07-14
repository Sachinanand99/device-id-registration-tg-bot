import os
import logging

from logging.handlers import RotatingFileHandler

# from https://t.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#your api id from https://my.telegram.org/apps
APP_ID = os.environ.get("APP_ID", "")

#your hash id from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "")

#your owner id from https://t.me/MissRose_bot reply her /id
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#don't change
PORT = os.environ.get("PORT", "8080")

#don't change
BOT_STATS_TEXT = os.environ.get("BOT_STATS_TEXT", "<b>BOT UPTIME</b>\n{uptime} 😼")

#don't change
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "Send /help for commands. \nYou nigger 🗿")

#don't change
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#your github userid 
GIT_USER_NAME = os.environ.get("GIT_USER_NAME", "")

#your github repo private or public
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", "")

#your github personal access token from https://github.com/settings/tokens classic recommended
GIT_PAT = os.environ.get("GIT_PAT", "") #"Contents" repository permissions read and write required

ADMINS = [] # seperated with whitespaces


#deployment
'''
1. pip install -r requirements.txt
2. configure config.py
3. python3 main.py or python main.py
'''



#no need to add anything from here.
WAIT_MSG="Pwease wait! 🤫"

try:
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
