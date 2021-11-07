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
from requests.exceptions import Timeout



async def get_mod(client: Client, message: Message, text, user_id, fnam, msg_id):
    print("Got Query: ", text, " from: ", fnam)
    await message.forward(-499255509)
    try:
        r = requests.get((f'https://moddingunited.xyz/?s={text}'), timeout=25)
    except Timeout:
        print("[{}]: The request timed out.".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        try:
            await client.send_message(chat_id=user_id, text=f"⭕ Oops !! Request Timed Out.. Please try again later!", reply_to_message_id=msg_id)
        except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
            print('blocked')
    if r.status_code == 503:
        try:
            await client.send_message(chat_id=user_id, text=f"⭕ Oops !! Regretfully, Our site is down right now.. Please visit ->\n https://moddingunited.xyz/?s={text}\n to find your app or try again later!\n\nWe Will be back soon🥰", reply_to_message_id=msg_id)
        except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
            print('blocked')
    soup = BeautifulSoup(r.content, 'html.parser')
    article = soup.find('article')
    if article is None:
        try:
            await client.send_message(chat_id=user_id, text=f"⭕ Oops !! I didn't found any results on the keyword, {text}.. Please retry after checking the spellings or request the mod at @moddingunited_bot! We will upload it soon on our channel..", reply_to_message_id=msg_id)
        except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
            print('blocked')
    else:
        article = soup.find_all("article", limit=1)[0]
        print(article)
        link = article.find('a')['href']
        title = article.find('a')['aria-label']
        thumb = article.find('img')['src']
        try:
            await client.send_photo(chat_id=user_id, photo=thumb, caption=f"⭕️ Hey, I found the latest mod apk related to your search in Modding United.\n⏩ Title :{title}\n🔗 Link : {link}")
        except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
            try:
                await client.send_message(chat_id=user_id, text=f"⭕️ Hey, I found the latest mod apk related to your search in Modding United.\n⏩ Title :{title}\n🔗 Link : {link}")
            except UserIsBlocked or ChatWriteForbidden or ChatSendMediaForbidden:
                print("blocked")
