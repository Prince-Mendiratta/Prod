""" MtProto Bot """

from pyrogram import (
    Client
)
from . import (
    TG_BOT_TOKEN,
    TG_BOT_WORKERS
)


if __name__ == "__main__":
    app = Client(
        ":memory:",
        bot_token=TG_BOT_TOKEN,
        plugins=dict(
            root="bot/plugins"
        ),
        workers=TG_BOT_WORKERS
    )
    app.set_parse_mode("html")
    app.run()