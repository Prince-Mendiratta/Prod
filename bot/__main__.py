""" MtProto Bot """

from pyrogram import (
    Client
)
from . import (
    API_HASH,
    APP_ID,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS
)


if __name__ == "__main__":
    app = Client(
        ":memory:",
        api_hash=API_HASH,
        api_id=APP_ID,
        bot_token=TG_BOT_TOKEN,
        plugins=dict(
            root="bot/plugins"
        ),
        workers=TG_BOT_WORKERS
    )
    app.set_parse_mode("html")
    app.run()
