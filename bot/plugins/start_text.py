from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AUTH_USERS,
    ONLINE_CHECK_START_TEXT,
)
from bot.sql.users_sql import (
    add_user_to_db,
    check_user_in_db,
    Users
)
from bot.sql import (
    SESSION
)
from sqlalchemy import func

@Client.on_message(
    filters.command("start"),
    group=3
)
async def num_start_message(client: Client, message: Message):
    START_OTHER_USERS_TEXT = """⭕ Hello, {}! To get started, Send me any the name of the APK that you want MODDED. I will perform a search in moddingunited.xyz for you & give you the results quickly..\n\n⚠️ Make sure you Enter the name of the app correctly with no spelling mistakes 😁\n\nFor more info, type /help!""".format(message.from_user.first_name)
    await message.reply_text(
        START_OTHER_USERS_TEXT,
        quote=True
    )
    q = check_user_in_db(message.from_user.id)
    if q == True:
        add_user_to_db(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.username
        )
        rows = SESSION.query(func.count(Users.chat_id)).scalar()
        print(rows)
        await client.send_message(chat_id=AUTH_USERS, text="🆕 New User!\nTotal: {}\nName: {}".format(rows[0],message.from_user.first_name))
        print("🆕 New User!\nTotal: {}\nName: {}".format(rows[0],message.from_user.first_name))
        SESSION.close()
    else:
        print('User in DB.')
        SESSION.close()


@Client.on_message(
    filters.command("help"),
    group=3
)
async def nimda_start_message(_, message: Message):
    await message.reply_text(
        ONLINE_CHECK_START_TEXT,
        quote=True
    )
