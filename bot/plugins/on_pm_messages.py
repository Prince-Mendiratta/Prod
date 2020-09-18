from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AUTH_USERS,
)
from pyrogram.errors.exceptions import UserIsBlocked
import telegram
import datetime
import requests
from bs4 import BeautifulSoup
from sqlalchemy import func



@Client.on_message(
    filters.private
)
async def on_pm_s(_, message: Message):
    await message.forward(-499255509)
    text = message.text
    user_id = message.from_user.id
    msg_id = message.message_id
    if text != "/start" or "/help":
        r = requests.get(f'https://moddingunited.xyz/?s={text}')
        soup = BeautifulSoup(r.content, 'html.parser')
        h1 = soup.find('h1')
        if "Nothing" in h1.text:
            try:
                await client.send_message(chat_id=user_id, text=f"⭕ Oops !! I didn't found any results on the keyword, {text}.. Please retry after checking the spellings or request the mod at @moddingunited_bot! We will upload it soon on our channel..", reply_to_message_id=msg_id)
            except UserIsBlocked:
                print('blocked')
        else:
            article = soup.find_all("article", limit=1)[0]
            link = article.find('a')['href']
            title = article.find('a')['title']
            thumb = article.find('img')['src']
            try:
                await client.send_photo(chat_id=user_id, photo=thumb, caption=f"⭕️ Hey, I found the latest mod apk related to your search in Modding United.\n⏩ Title :{title}\n🔗 Link : {link}")
            except UserIsBlocked:
                print("blocked")
    pp = check_user_in_db(user_id)
    if pp = False:
        add_user_to_db(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.username
        )
        rows = session.query(func.count(Users.chat_id)).scalar()
        await client.send_message(chat_id=742506768, text="🆕 New User!\nTotal: {}\nName: {}".format(rows,message.from_user.first_name))
    else:
        print('User in DB.')