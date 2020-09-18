from pyrogram import (
    Client,
    filters
)
from request import get_mod


@Client.on_message(
    filters.private
)
async def on_pm_s(client: Client, message: Message):
    get_mod(client, message)
