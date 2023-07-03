import os
from telethon import Button
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from alpha import __version__


# Main Details
API_ID = 19611094
API_HASH = "c5198b0dab5cdd8e0eaaf3e0c742fbd3"
BOT_TOKEN = '5561096520:AAG85BkelBhEsXtJSG1HFx2mWlX4ouMIbTY'
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alpha_movie_finder_bot")
INLINE_THUMB = os.environ.get("INLINE_THUMB", "https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg")
BOT_STARTED = '''
`
╭━━━┳╮╱╱╱╭╮
┃╭━╮┃┃╱╱╱┃┃
┃┃╱┃┃┃╭━━┫╰━┳━━╮
┃╰━╯┃┃┃╭╮┃╭╮┃╭╮┃
┃╭━╮┃╰┫╰╯┃┃┃┃╭╮┃
╰╯╱╰┻━┫╭━┻╯╰┻╯╰╯
╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╰╯`
{}
Powered By Pyrogram & Telethon
Using Firebase as a Database
Developed By Team Alpha  

{}
'''
STMSG="""[👋](https://telegra.ph/file/a1d57aa7a5c4f0401667b.jpg)  Hey there {},

I am {}, an  Advanced Movie Finder Bot For help to Find Movies. 

{}
"""

HLPMSG='''⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊
Available Types:

#report: If you want to report errors,Bugs or Something, mention #report and send it to this bot

Use This Format - #report {My Bug}
Ex: #report example bug

How To Search Movies: Go To Inline Or Send Me Your Movie Name Ex: 'Avengers EndGame 2019 720p'

/start: Start the bot

/info: Get information about the Replyed User

/help: Display the available commands and their descriptions

/count: Get User List And Status (Admin Command)

/bpromo: Promote User As Bot Admin (Admin Command)

/bdemo: Demote User As Bot Admin (Admin Command)

/broadcast: Broadcast Message Via Bot (Admin Command)

/ban: /unban {user_id} Ban Usr From Bot (Admin Command)

/unban: /unban {user_id} Remove Man From User(Admin Command)

/listbanned: Get List Of Banned Users(Admin Command)'''
LOG_CHNL = -1001689365631
START_TEXT="""[👋](https://telegra.ph/file/a1d57aa7a5c4f0401667b.jpg)  Hey there {},

I am 𝙰𝙻𝙿𝙷𝙰 Movie Finder bot, an  Advanced Movie Finder Bot For help to Find Movies. 

"""

ABOUT_TEXT="""
 ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇꜱᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄʟᴇʀᴀ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ᴀᴛ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/AlphaTm_Botz_chat) 

ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ [Tᴇᴀᴍ ᴀʟᴘʜᴀ](https://t.me/Team_Alpha_Devs)
"""

ADMIN_TOOLS='**ADMIN menu** \n\nHere are some of the docs about Admin Cmd .'

BAN_TEXT="""**✘ Bans and Other

‣ `/ban` - To Ban Someone from a chat.
‣ `/unban` - To unban a member from the chat.
"""
INFO_TEXT="""info
"""
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

CL_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton("Close",callback_data="cls")
                 ]
                 ])

HELP_KEY= InlineKeyboardMarkup([[              
                 InlineKeyboardButton(' Team ┊𝙰𝙻𝙿𝙷𝙰 么 ', url="https://t.me/Team_Alpha_Devs")
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

CHANNEL_LINK = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('💌 Channel 1 (First Join Here)', url='https://t.me/AlphaTm_Botz'),
            InlineKeyboardButton('💌 Channel 2 (And Join Here)', url='https://t.me/AlphaRedirecttoMain')
        ],
        [
            InlineKeyboardButton('🎡 Support Group', url='https://t.me/AlphaTm_Botz_chat')
        ],
        [
            InlineKeyboardButton('♻️ Refresh ♻️', callback_data='ref')
        ]
    ]
)


USER_NOT="""🚫 Access Denied
hey {} ,
you must join [Our Channell](https://t.me/AlphaTm_Botz).
so ,please join and try again 
"""


Admin = "Admin"
formatting = "formatting"
F_sub = "F-Sub"
Approval = "Approval"
Restrict = "Restrict"
Blacklists = "Blacklists"
Extra = "Extra"
Chat_Bot = "Chat-Bot"
Connections = "Connections"
Federations = "Federations"
Filter = "Filters"
Protection = "Protection"
Languages = "Languages"
Locks = "Locks"
Nightmode = "N-Mode"
Note = "Notes"
Pin = "Pin"
Purges = "Purge"
Reports = "Reports"
Rule = "Rules"
Sticker = "Sticker"
Tagalert = "Tagalert"
Warnin = "Warnings"
Greeting = "Greetings"
