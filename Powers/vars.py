from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=5979235760:AAGQUEYP24tv3qXLksQlUXxaYQm2OmNbCPU)
    API_ID = int(config("API_ID", default="29024923"))
    API_HASH = config("API_HASH", default=5f917f1d096939dc6b282ef40e922827)
    OWNER_ID = int(config("OWNER_ID", default=1071294954))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="1071294954",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="1071294954",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1344569458",
        ).split(" ")
    ]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5979235760:AAGQUEYP24tv3qXLksQlUXxaYQm2OmNbCPU"
    API_ID = 29024923  # Your APP_ID from Telegram
    API_HASH = "5f917f1d096939dc6b282ef40e922827"  # Your APP_HASH from Telegram
    OWNER_ID = 1071294954  # Your telegram user id defult to mine
    MESSAGE_DUMP = -100  # Your Private Group ID for logs
    DEV_USERS = [1071294954]
    SUDO_USERS = [1071294954]
    WHITELIST_USERS = [1071294954]
    DB_URI = "mongodb+srv://qashidark:Ayesha.Qasim1@cluster0.3ywjjzu.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "Cluster0"  # Your DB name
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "redhatgroup"
    SUPPORT_CHANNEL = "redhatworldcom"
    VERSION = "VERSION"
    WORKERS = 8
