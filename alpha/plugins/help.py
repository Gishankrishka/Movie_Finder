from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha.helpers.funcs import *
from alpha import pbot, tbot
from alpha.__version__ import __version__, __copyright__, __license__ 
from telethon import events, Button

command_descriptions = {
    "#report": "If you want to report errors,Bugs or Something, mention #report and send it to this bot\n\nUse This Format - #report {My Bug}\nEx: #report example bug",
    "How To Search Movies": "Go To Inline Or Send Me Your Movie Name Ex: '`Avengers EndGame 2019 720p`'",
    "/start": "Start the bot",
    "/info": "Get information about the Replyed User",
    "/help": "Display the available commands and their descriptions",
    "/count": "Get User List And Status (Admin Command)",
    "/bpromo": "Promote User As Bot Admin (Admin Command)",
    "/bdemo": "Demote User As Bot Admin (Admin Command)",
    "/broadcast": "Broadcast Message Via Bot (Admin Command)",
    "/ban": "`/unban {user_id}` Ban Usr From Bot (Admin Command)",
    "/unban": "`/unban {user_id}` Remove Man From User(Admin Command)",
    "/listbanned": "Get List Of Banned Users(Admin Command)",
    # Add more commands and descriptions as needed
}

tbk =[
     [Button.inline('Close', data='cls')]]

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(' Team ┊𝙰𝙻𝙿𝙷𝙰 么 ', url="https://t.me/+jrqciS7XvKNhODc1")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 License 🌴",callback_data="lsn")
                 ],
                 [
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ 🍄", url="https://github.com/TeamAlphaTg")
                 ],
                 [
                 InlineKeyboardButton('Search Movies 🔎', switch_inline_query_current_chat="")
                 ]
                 ]
                )

@pbot.on_message(filters.command(["help"]))
async def help_command(bot, update):
        if await forcesub( bot,update):
            return
        # Generate the help message using the command_descriptions dictionary
        help_text = "⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊\n<b>Available Types:</b>\n\n"
        for command, description in command_descriptions.items():
            help_text += f"<b>{command}</b>: {description}\n\n"
        
        # Send the help message as a reply to the /help command
        await update.reply_text(help_text, reply_markup=START_BUTTON)


@tbot.on(events.callbackquery.CallbackQuery(data="lsn"))
async def _(event):

     await event.edit(f'{__license__}\n\n{__copyright__}', buttons=tbk)         
