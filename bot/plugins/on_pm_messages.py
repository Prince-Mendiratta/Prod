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
import datetime
import requests
from bs4 import BeautifulSoup
from sqlalchemy import func



@Client.on_message(
    filters.private
)
async def on_pm_s(client: Client, message: Message):
    text = message.text
    user_id = message.from_user.id
    fnam = message.from_user.first_name
    msg_id = message.message_id
    if text == "/start" or "/help":
        continue
    else:
        await message.forward(-499255509)
        print("Got Query: ", text, " from: ", fnam)
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
