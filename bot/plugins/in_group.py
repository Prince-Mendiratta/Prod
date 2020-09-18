from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked, CHAT_WRITE_FORBIDDEN, CHAT_SEND_MEDIA_FORBIDDEN
from request import get_mod


@Client.on_message(
    filters.group &
    filters.command("mod", ["/", "!"]),
    group = 3
)
async def group_wala(client: Client, message: Message):
    try:
        get_mod(client, message)
    except CHAT_WRITE_FORBIDDEN or CHAT_SEND_MEDIA_FORBIDDEN:
        print('Limited Rights')
