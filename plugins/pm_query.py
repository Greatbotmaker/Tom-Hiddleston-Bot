# ---------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------- #

import re
import os
import time

from bot import Bot
from presets import Presets
from base64 import b64decode
from helper.file_size import get_size
from helper.forcesub import ForceSub
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

if os.environ.get("ENV", False):
    from configs import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.command("start"))
async def start_handler(bot: Client, event: Message):
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await event.reply_text(
        text=f"Hi, {event.from_user.mention}\n{Config.START_TEXT}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Main Group", url="https://t.me/OB_MOVIESGROUP"),
                 InlineKeyboardButton("Main Channel", url="https://t.me/OB_Links")],
                [InlineKeyboardButton("Developer - @OwDvEr_BoT", url="https://t.me/OwDvEr_BoT")]
            ]
        )
    )
        except Exception:
            pass
        return
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text=Config.START_TEXT,
            parse_mode='html',
            disable_web_page_preview=True
        )
        if secret_query:
            for channel in Config.CHANNELS:
                # Looking for Document type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="document", limit=50):
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
                                caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_DOC.format(media_name,
                                                                                            media_format, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
                # Looking for video type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="video", limit=50):
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
                                caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_VID.format(media_name, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
    except Exception:
        return
