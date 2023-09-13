from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.__version__ import __version__, __copyright__, __license__ 
from telethon import events, Button

@pbot.on_message(filters.command(['license', 'lsn']))
async def help(bot, m):
  await m.reply_text(f'{__license__}\n\n{__copyright__}', reply_markup=CL_BTN, quote=True)
