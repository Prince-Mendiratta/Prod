from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked, ChatWriteForbidden, ChatSendMediaForbidden
from bot.hf.request import get_mod


@Client.on_message(
    filters.group &
    filters.command("mod", ["/", "!"]),
    group = 3
)
async def group_wala(client: Client, message: Message):
    intro = str(message.text)
    cmds, query = intro.split(' ', 1)
    text = str(query)
    user_id = message.chat.id
    fnam = message.from_user.first_name
    msg_id = message.message_id
    await get_mod(client, message, text, user_id, fnam, msg_id)
