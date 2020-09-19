from pyrogram import (
    Client,
    filters
)
from bot.hf.request import get_mod
from pyrogram.types import Message
from bot.plugins.start_text import nimda_start_message, num_start_message



@Client.on_message(
    filters.private
)
async def on_pm_s(client: Client, message: Message):
    text = str(message.text)
    user_id = message.from_user.id
    fnam = message.from_user.first_name
    msg_id = message.message_id
    if text == "/start":
        num_start_message(client,message)
    elif text == "/help" or "/mod":
        nimda_start_message('a', message)
    else:
        await get_mod(client, message, text, user_id, fnam, msg_id)
