import re
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from bot import configs, VERIFY # pylint: disable=import-error
from bot.helper.forcesub import ( # pylint: disable=import-error

@Client.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
        InlineKeyboardButton('➕ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕', url=f'http://t.me/OB_FILTERBOT?startgroup=botstart')
        ],[
        InlineKeyboardButton('👨🏻‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢', url=f't.me/OB_LINKS')
    ],[
        InlineKeyboardButton('🔧 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('𝙷𝙴𝙻𝙿 ⚙️', callback_data="help")
    ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )
    
    elif query_data == "help":
        buttons = [[
            InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
            InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🚩', callback_data='about')
        ],[
            InlineKeyboardButton('🔐 𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.HELP_TEXT,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "about": 
        buttons = [[
            InlineKeyboardButton('👨🏻‍💻 𝙾𝚠𝙳𝚟𝙴𝚛', url='https://t.me/OWDVER_BOT'),
            InlineKeyboardButton('👨🏻‍💻 𝙴𝚒𝚗𝚜𝚝𝚎𝚒𝚗', url='https://t.me/AlbertEinstein_TG')
        ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()
