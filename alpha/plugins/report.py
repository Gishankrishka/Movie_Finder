from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.funcs import *
from alpha.helpers.db import *
from alpha.__version__ import __version__, __license__, __copyright__ 




@pbot.on_message(filters.regex(pattern="#report"))   
async def startprivate(bot, message):
    if len(message.text.split()) == 1:
        await message.reply_text('Use This Format -  `#report {My Bug}`\n\nEx:  `#report example bug`')
    else:
        t = message.text.replace('#report', " ")
        data = GetAdmins()
        await pbot.send_message(LOG_CHNL, f"#report From user {message.from_user.mention},\n\n`{t}`\n\n\n")
        for key, val in data.items():
            try:
                m =await pbot.send_message(key, f"#report From user {message.from_user.mention},\n\n`{t}`")
            except:
                await m.delete()
                await pbot.send_message(val, f"#report From user {message.from_user.mention},\n\n`{t}`")
                
            