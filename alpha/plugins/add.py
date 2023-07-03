from pyrogram.types import InlineQueryResultVideo
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__ 
from pyrogram import filters
import uuid



media_filter = filters.document | filters.video | filters.audio

@pbot.on_message(filters.chat(-916273960) & media_filter)
async def addtodb(bot, message):
    document = message.document
    file_name = document.file_name
    file_id = document.file_id
    file_size = document.file_size
    caption = message.caption
    random_file_id = str(uuid.uuid4())
    if IsAdmin(message.from_user.id):
        movie_name = str(file_name)
        key = random_file_id
        movie_details = {
            "Title": f"{movie_name}",
            "FileId": f"{file_id}",
            "Size": f"{file_size}",
            "Caption":f"{caption}" 
        }
        AddMvs(key, movie_details)
        await message.reply_text(f'`{movie_name}` **Added To Database Succesfuly!**')
    else:
        await message.reply_text(f"Eww [{message.from_user.first_name}](tg://user?id={message.from_user.id}), Don't Touch Me Ur Not My Admin")
        
@pbot.on_message(filters.chat(-1001567630499) & media_filter)
async def addtodb(bot, message):
    document = message.document
    file_name = document.file_name
    file_id = document.file_id
    file_size = document.file_size
    caption = message.caption
    random_file_id = str(uuid.uuid4())
    movie_name = str(file_name)
    key = random_file_id
    movie_details = {
        "Title": f"{movie_name}",
        "FileId": f"{file_id}",
        "Size": f"{file_size}",
        "Caption":f"{caption}" 
    }
    AddMvs(key, movie_details)    

    