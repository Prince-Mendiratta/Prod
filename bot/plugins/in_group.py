from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked, ChatWriteForbidden, ChatSendMediaForbidden
from bot.hf.request import get_mod
from bot.plugins.start_text import nimda_start_message, num_start_message


@Client.on_message(
    filters.group &
    filters.command("mod", "/")
)
async def group_wala(client: Client, message: Message):
    intro = str(message.text)
    try:
        cmds, query = intro.split(' ', 1)
        text = str(query)
        user_id = message.chat.id
        fnam = message.from_user.first_name
        msg_id = message.message_id
        if text != "/start" or "/help":
            await get_mod(client, message, text, user_id, fnam, msg_id)
        elif text == "/start":
            await num_start_message(client,message)
        elif text == "/help":
            await nimda_start_message('a', message)
    except:
        0+0
