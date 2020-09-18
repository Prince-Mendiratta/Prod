from pyrogram import (
    Client,
    filters
)
from pyrogram.errors.exceptions import UserIsBlocked, ChatWriteForbidden, ChatSendMediaForbidden
import datetime
import requests
from bs4 import BeautifulSoup
from sqlalchemy import func
from pyrogram.types import Message

text=user_id=fnam=msg_id = ' '
async def get_mod(client: Client, message: Message):
    if text != '/start':
        print("Got Query: ", text, " from: ", fnam)
        await message.forward(-499255509)
        r = requests.get(f'https://moddingunited.xyz/?s={text}')
        soup = BeautifulSoup(r.content, 'html.parser')
        h1 = soup.find('h1')
        if "Nothing" in h1.text:
            try:
                await client.send_message(chat_id=user_id, text=f"⭕ Oops !! I didn't found any results on the keyword, {text}.. Please retry after checking the spellings or request the mod at @moddingunited_bot! We will upload it soon on our channel..", reply_to_message_id=msg_id)
            except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
                print('blocked')
        else:
            article = soup.find_all("article", limit=1)[0]
            link = article.find('a')['href']
            title = article.find('a')['title']
            thumb = article.find('img')['src']
            try:
                await client.send_photo(chat_id=user_id, photo=thumb, caption=f"⭕️ Hey, I found the latest mod apk related to your search in Modding United.\n⏩ Title :{title}\n🔗 Link : {link}")
            except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
                try:
                    await client.send_message(chat_id=user_id, text=f"⭕️ Hey, I found the latest mod apk related to your search in Modding United.\n⏩ Title :{title}\n🔗 Link : {link}")
                except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
                    print("blocked")
    else:
        0+0