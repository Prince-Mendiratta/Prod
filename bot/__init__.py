""" credentials """

from .get_config import get_config


API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# array to store the channel ID who are authorized to use the bot
AUTH_USERS = list(set(
    int(x) for x in get_config(
        "AUTH_USERS",
        should_prompt=True
    ).split()
))
# sqlalchemy Database for the bot to operate
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
# check online status of your bot
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        """⭕ To use this bot, you just need to send the name of the application that you want modded. We will run a query to search for the MODDED app at moddingunited.xyz & give you the search results.\n\n⚠️ If you cannot find the app you're looking for, it's possible we haven't uploaded it on the website yet. You can leave a message at @ModdingUnited_Bot and our team will have a look.\n\n🧐 In case of any issues, you can email us at info@moddingunited.xyz and we'll get back to you soon!"""
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
