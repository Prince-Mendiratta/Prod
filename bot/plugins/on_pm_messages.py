from pyrogram import (
    Client,
    filters
)
from bot.plugins.request import get_mod
from pyrogram.types import Message



@Client.on_message(
    filters.private
)
async def on_pm_s(client: Client, message: Message):
    text = str(message.text)
    user_id = message.from_user.id
    fnam = message.from_user.first_name
    msg_id = message.message_id
    await get_mod(client, message)
