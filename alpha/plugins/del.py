from pyrogram.types import InlineQueryResultCachedDocument
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@pbot.on_message(filters.command('del'))
async def delete_files_by_name(client, message):
    # Extract the movie name from the command
    movie_name = message.text.split(' ', 1)[1].strip()
    data = GetMvs()
    keyboard = []
    if IsAdmin(message.from_user.id):
        found_files = False  # Flag to track if any files were found for the given movie name
        for key, val in data.items():
            movie_title = replace_invalid_characters(val.get("Title", ""))
            if movie_name.lower() in movie_title.lower():
                found_files = True
                button = InlineKeyboardButton(val.get("Title", ""), callback_data=f'delete:{key}')
                keyboard.append([button])

        if found_files:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await message.reply_text('Select the file to delete:', reply_markup=reply_markup)
        else:
            await message.reply_text('No files found for the given movie name.')
    else:
        await message.reply_text('You are not authorized to delete files.')

       