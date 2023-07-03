from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.funcs import *
from alpha.helpers.db import *
from alpha.__version__ import __version__, __license__, __copyright__ 
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

HELP_KEY = InlineKeyboardMarkup([[              
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
@pbot.on_message(filters.new_chat_members)
async def handle_new_chat_members(client, message):
    for user in message.new_chat_members:
        me = await client.get_me()
        if user.id == me.id:
            group = await client.get_chat(message.chat.id)
            await AddNewGroup(str(group.title), int(message.chat.id))
            await message.reply_text(f"Thankyou For Adding Me To {group.title} ❣️If you have any questions & doubts about using me contact support.\nUse the `/addmme {message.chat.id}` command to start sending movies in this group\n\n**Don't forget to make me admin**", 
            reply_markup =InlineKeyboardMarkup([[              
                         InlineKeyboardButton(' Team ┊𝙰𝙻𝙿𝙷𝙰 么 ', url="https://t.me/+jrqciS7XvKNhODc1")
                         ],
                         [
                         InlineKeyboardButton(text="🌴 Help 🌴",callback_data="help"),
                         InlineKeyboardButton("🍄 License 🍄", callback_data="https://github.com/TeamAlphaTg")
                         ],
                         [
                         InlineKeyboardButton('Search Movies 🔎', switch_inline_query_current_chat=""),
                         InlineKeyboardButton('🌝 Share Us 🌝', switch_inline_query="bshare"),
                         ]
                         ]
                        ))


@pbot.on_message(filters.group & filters.command(["start"]))
async def gstart(bot, update):
    if await forcesub( bot,update):
        return
    group = await bot.get_chat(update.chat.id)
    await AddNewGroup(str(group.title), int(update.chat.id))
    await AddNewUser(str(update.from_user.username), int(update.from_user.id))
    me = await bot.get_me()
    await update.reply_text("Send Me A Movie Name To Find",
    reply_markup =InlineKeyboardMarkup([[              
                         InlineKeyboardButton('DM Me', url=f"https://t.me/{me.username}?start=help")
                         ]
                         ]
                        ))

@pbot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if await forcesub( bot,update):
        return
    await AddNewUser(str(update.from_user.username), int(update.from_user.id))
    if len(update.text.split()) > 1:
        text = (update.text.split(None, 1)[1]).lower()
        if text=='help':
            await update.reply_text(HLPMSG,reply_markup=HELP_KEY)
        if text=='force':
            await update.reply_sticker('CAACAgUAAxkBAAETyzhkmxKvk0odqy8SXVgxamivUsTuWgACEAQAAuI_cVVsR2VjcwHrNS8E')
            await update.reply_text(USER_NOT.format(update.from_user.mention),reply_markup=CHANNEL_LINK)
        elif text=="inlinest":
            await update.reply_text('**Go Inline Or Give Me Some NAme To Find**',reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('Search Inline ', switch_inline_query_current_chat="")
                 ],
                 [             
                 InlineKeyboardButton('ℹ️ About ', callback_data="about"),
                 InlineKeyboardButton("🌴 Help And Commands ",callback_data="help")
                 ],
                 [
                 InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="https://t.me/Team_Alpha_Devs")
                 ],
                 [
                 InlineKeyboardButton('🌝 Share Us 🌝', switch_inline_query="bshare"),
                 ]
                 ]
                  ))
        else:
            data = GetMvs() 
            movie_file_id = data.get(text, {}).get("FileId", "") 
            kb = int(data.get(text, {}).get("Size", "") )
            inkb = kb / 1048576
            movie_size = "{:.2f}".format(inkb)
            movie_title = data.get(text, {}).get("Title", "") 
            movie_caption = data.get(text, {}).get("Caption", "") 
            caption = f"Name: `{movie_title}`'\nSize: `{movie_size} MB`\nCaption: `{movie_caption}`"
            await pbot.send_document(chat_id=update.chat.id,caption=caption, document=movie_file_id)        

    else:
        await AddNewUser(str(update.from_user.username), int(update.from_user.id))
        me=await bot.get_me()
        uname=me.username
        await update.reply_text(STMSG.format(update.from_user.mention, __version__, __copyright__) ,reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('➕ Add Me To Your Group ➕ ', url=f"http://t.me/{uname}?startgroup=new")
                 ],
                 [             
                 InlineKeyboardButton('ℹ️ About ', callback_data="about"),
                 InlineKeyboardButton("🌴 Help And Commands ",callback_data="help")
                 ],
                 [
                 InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="t.me/Team_Alpha_Devs")
                 ],
                 [
                 InlineKeyboardButton('🌝 Share Us 🌝', switch_inline_query="bshare"),
                 ]
                 ]
                  ))
        
