# -----------------------------------------------------------------|| https://github.com/owdver/DQ40 ||----------------------------------------------------------------- #
import re
import os
import time
import psutil
import shutil
import string
import asyncio
from pyromod import listen
from pyrogram import Client, filters
from base64 import b64decode
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from bot import Bot
from presets import Presets
from configs import Config
from helper.file_size import get_size
from helpers.database.access_db import db
from helpers.forcesub import ForceSub
from helpers.broadcast import broadcast_handler
from helpers.database.add_user import AddUserToDatabase


DQ = Client(
    session_name=Config.USER_SESSION,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


@DQ.on_message(filters.private & filters.command("start"))
async def start_handler(client: Bot, message: Message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply_text(
        text=f"Hi, {message.from_user.mention}\n{Config.START_TEXT}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
        InlineKeyboardButton('➕ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕', url=f'http://t.me/OB_FILTEROBOT?startgroup=botstart')
        ],[
        InlineKeyboardButton('👨🏻‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢', url=f't.me/OB_LINKS')
    ],[
        InlineKeyboardButton('🧑‍💻 DEV', url=f't.me/space4renjith'),
        InlineKeyboardButton('𝙷𝙴𝙻𝙿 ⚙️', callback_data="help")]
            ]
        )
    )
    try:
        if secret_query:
            for channel in Config.CHANNELS:
                # Looking for Document type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="document", limit=30):
                    doc_file_names = messages.document.file_name
                    file_size = get_size(messages.document.file_size)
                    if re.compile(rf'{doc_file_names}', re.IGNORECASE):
                        media_name = messages.document.file_name.rsplit('.', 1)[0]
                        media_format = messages.document.file_name.split('.')[-1]
                        await client.send_chat_action(
                            chat_id=message.from_user.id,
                            action="upload_document"
                        )
                        try:
                            await client.copy_message(
                                chat_id=message.chat.id,
                                from_chat_id=messages.chat.id,
                                message_id=messages.message_id,
                                caption=Config.BOTTOM_CAPTION+Presets.CAPTION_TEXT_DOC.format(media_name,
                                                                                            media_format, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
                # Looking for video type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="video", limit=30):
                    vid_file_names = messages.caption
                    file_size = get_size(messages.video.file_size)
                    if re.compile(rf'{vid_file_names}', re.IGNORECASE):
                        media_name = secret_query.upper()
                        await client.send_chat_action(
                            chat_id=message.from_user.id,
                            action="upload_video"
                        )
                        try:
                            await client.copy_message(
                                chat_id=message.chat.id,
                                from_chat_id=messages.chat.id,
                                message_id=messages.message_id,
                                caption=Config.BOTTOM_CAPTION+Presets.CAPTION_TEXT_VID.format(media_name, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
    except Exception:
        return
