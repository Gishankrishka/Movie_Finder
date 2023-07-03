from pyrogram.types import InlineQueryResultCachedDocument
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__


@pbot.on_message(filters.command("addme"))
async def adme(bot, message):
    parts = message.text.split()
    if len(parts) == 1:
        await message.reply_text(f"Dear {message.from_user.mention}, you should use this format ---> \n`/addme group_id`\n\n`/addme -100168936563`")
    else:
        id = parts[1]
        if str(id).startswith("-"):
            try:
                group = await bot.get_chat(id)
                AddmGroup(str(group.title), int(id))
                await message.reply_text(f"Succesfully added `{group.title}` to the database")
            except Exception as e:
                await SendLog(e, message.from_user.first_name, message.from_user.id, message.chat.id)
        else:
            await message.reply_text("Please use this command with group IDs")


@pbot.on_message(filters.command("remme"))
async def reme(bot, message):
    try:
        if len(message.text.split()) == 1:
            chat_id = message.chat.id
        else:
            parts = message.text.split()
            chat_id = parts[1]
            
        Remmgroup(chat_id)
        group = await bot.get_chat(chat_id)
        await message.reply_text(f"Successfully removed `{group.title}` from the database")
    except Exception as e:
        await SendLog(e, message.from_user.first_name, message.from_user.id, message.chat.id)
