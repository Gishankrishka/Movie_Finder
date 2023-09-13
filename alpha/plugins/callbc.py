from pyrogram import filters
from var import *
from alpha.helpers.funcs import *
from alpha.helpers.db import *
from alpha import tbot, pbot
from alpha.__version__ import __version__, __copyright__, __license__ 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Optional
from pyrogram import filters, emoji
from pyrogram.errors.exceptions.bad_request_400 import (
    MessageIdInvalid, MessageNotModified
)
from pyrogram.types import (
    User,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery,
)

import json

try:
    with open('data.json') as f:
        whispers = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    whispers = {}
open('data.json', 'w').close()
@tbot.on(events.CallbackQuery(data='genuserlist'))
async def UserAndGroupsGen(e):
	c = await e.get_chat()
	m = await e.get_message()
	await GetUsrsGrpsToTxt(c)
	await m.delete()
@tbot.on(events.CallbackQuery(data='genbuserlist'))
async def UserAndGroupsGen(e):
	c = await e.get_chat()
	m = await e.get_message()
	await GetBAnsToTxt(c)
	await m.delete()

START_KEY=InlineKeyboardMarkup([[
                 InlineKeyboardButton('➕ Add Me To Your Group ➕ ', url="http://t.me/Alpha_GroupHelp_Bot?startgroup=new")
                 ],
                 [             
                 InlineKeyboardButton('ℹ️ About ', callback_data="about"),
                 InlineKeyboardButton("🌴 Help And Commands ",callback_data="help")
                 ],
                 [
                 InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="https://t.me/Team_Alpha_Devs")
                 ]
                 ]
                  )

BACK_BUTTON=InlineKeyboardMarkup([[              
                 InlineKeyboardButton(' 🔙 back', callback_data="home")
                 ]]
                  )

@pbot.on_callback_query()
async def cb_handler(bot, update):
    me=await bot.get_me()
    uname=me.username
    callback_data = update.data.split(":")
    if update.data == "help":
      await update.message.edit_text(
            text=HLPMSG,
            reply_markup=HELP_KEY,
            disable_web_page_preview=True
        )
    
    elif update.data == "home":
      await update.message.edit_text(STMSG.format(update.from_user.mention, __version__, __copyright__),
             reply_markup=START_KEY)

    elif update.data == "about":
      await update.message.edit_text(ABOUT_TEXT.format(uname),
             reply_markup=BACK_BUTTON)
    
    elif update.data == "info":
      await update.message.edit_text(INFO_TEXT,
              reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton(' « Back', callback_data="help")
                 ]]
                  ))
    
    elif update.data == "ban":
      await update.message.edit_text(BAN_TEXT,
              reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton(' « Back', callback_data="help")
                 ]]
                  ))
    elif update.data == "cls":
      await update.message.delete() 
    elif update.data == "close_data":
      await update.message.delete()
    elif update.data == "requ":
      await pbot.send_message(update.message.chat.id, "**Enter Your Movie Name**")
      response = await pbot.listen(update.message.chat.id)
      msg = response.text
      Admins = GetAdmins()   
      for key in Admins:
        try:
              await pbot.send_message(key, f'**⚠️Request From User! [{update.from_user.first_name}](tg://user?id={update.from_user.id})⚠️**\n **Plz Add Given Film To Db**\n\nFrom User: `{update.from_user.id}`\n Film Name: `{msg}`')
              await pbot.send_message(update.message.chat.id, "**Your Request Successfully Sent**")
        except Exception as e:
              await SendLog(e, update.from_user.first_name, update.from_user.id, update.message.chat.id)

    elif update.data == "banrq":
        await pbot.send_message(update.message.chat.id, "**Enter Your Message**")
        response = await pbot.listen(update.message.chat.id)
        msg = response.text
        Admins = GetAdmins()   
        await pbot.send_message(LOG_CHNL, f'**⚠️Request From Banned User! [{update.from_user.first_name}](tg://user?id={update.from_user.id})⚠️**\n\nFrom User: `{update.from_user.id}`\n Message: `{msg}`')
        for key in Admins:
            try:
                await pbot.send_message(key, f'**⚠️Request From Banned User! [{update.from_user.first_name}](tg://user?id={update.from_user.id})⚠️**\n\nFrom User: `{update.from_user.id}`\n  Message: `{msg}`')
                  
            except Exception as e:
                await SendLog(e, update.from_user.first_name, update.from_user.id, update.message.chat.id)
        await pbot.send_message(update.message.chat.id, "**Your Request Successfully Sent**")
        await update.message.delete()  
    elif update.data == "ref": 
        await update.answer("♻️Reloading.....♻️",) 
        await update.message.delete()
        await pbot.delete_messages(update.message.chat.id, message_ids=int(int(update.message.id)-1))
        if await forcesub_cl(bot, update):
            return
        file_id = "CAADAQADlwEAAv2w4EVrWcNQPe8AATQC"
        reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Search Inline ', switch_inline_query_current_chat="")
                 ],
                 [             
                 InlineKeyboardButton('ℹ️ About ', callback_data="about"),
                 InlineKeyboardButton("🌴 Help And Commands ",callback_data="help")
                 ],
                 [
                 InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="https://t.me/Team_Alpha_Devs")
                 ]
                 ]
                  )
        await bot.send_message(
            update.message.chat.id,
            text=START_TEXT.format(update.message.from_user.mention),
            reply_markup=reply_markup
        )
    
    elif update.data.startswith('delete:'):
        key = update.data.split(':', 1)[1]
        RemMvs(key)
        await update.answer('File deleted successfully!')
        await update.message.delete()
    elif callback_data[0] == "select_movie":
        users = All.order_by_key().equal_to(str(update.from_user.id)).get()
        print(users)
        if users:  
            await update.answer(f"Plz Wait....")
            key = callback_data[1]
            url=f"http://t.me/Alpha_movie_finder_bot?start={key}"
            data = GetMvs() 
            movie_file_id = data.get(key, {}).get("FileId", "") 
            kb = int(data.get(key, {}).get("Size", "") )
            inkb = kb / 1048576
            movie_size = "{:.2f}".format(inkb)
            movie_title = data.get(key, {}).get("Title", "") 
            movie_caption = data.get(key, {}).get("Caption", "") 
            caption = f"Name: `{movie_title}`'\nSize: `{movie_size} MB`\nCaption: `{movie_caption}`"
            await update.answer(f"Sending....")
            await pbot.send_document(chat_id=update.message.chat.id,caption=caption, document=movie_file_id, reply_markup=InlineKeyboardMarkup([[
                     InlineKeyboardButton('Shareable Link 🔗', url=url)
                     ],
                     [             
                     InlineKeyboardButton("Share Link",url='https://t.me/share/url?url={url}')
                     ]
                     ]
                      ))
        else:
             print("NFS")    
    elif update.data =="notvs":
        mm = update.message.text.replace(' ', '%20')
        await bot.edit_message_text(
            chat_id=update.message.chat.id,
            message_id=update.message.id,
            text=f"**No Results Found In Our Database\nCheck Spelling On [Google](https://www.google.com/search?q={mm})",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Request 👤", callback_data="requ")
            ],
                [
                    InlineKeyboardButton("Search On Google 🌐", url=f"https://google.com/search?q={mm}/movie")
                ],
                [
                    InlineKeyboardButton("Click Here To Find Release Data 📅",
                                         url=f"http://www.google.com/search?q={mm}%20movie%20Release%20Date")
                ]
            ]
            ))
    elif update.data =="tsinfo":
        print(update.id)
        await bot.answer_callback_query(
        update.id,
        text='''
----------------------------------
TV Series Request Format
----------------------------------
        
Format :- S{season}E{episode}
Example :- The Good Doctor S01E01
        ''',
        show_alert=True
    )