from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked, ChatWriteForbidden, ChatSendMediaForbidden
from bot.plugins.request import get_mod


@Client.on_message(
    filters.group &
    filters.command("mod", ["/", "!"]),
    group = 3
)
async def group_wala(client: Client, message: Message):
    get_mod(client, message)
