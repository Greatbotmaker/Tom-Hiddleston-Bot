# -----------------------------------------------------------------|| https://github.com/owdver/DQ40 ||----------------------------------------------------------------- #

import re
import os
import time

from bot import Bot
from presets import Presets
from base64 import b64decode
from helper.file_size import get_size
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

if os.environ.get("ENV", False):
    from configs import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client: Bot, message: Message):
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
        except FloodWait as e:
            time.sleep(5)  
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Uploading....",
            parse_mode='html'
        )
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
                                caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_DOC.format(media_name,
                                                                                            media_format, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(86400)
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
                                caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_VID.format(media_name, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(86400)
    except Exception:
        return
