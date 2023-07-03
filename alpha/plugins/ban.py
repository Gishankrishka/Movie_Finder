from logging import exception
from pyrogram import filters, Client
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid
from pyrogram.types import ChatPrivileges
from alpha import pbot
from pyrogram.types import InlineQueryResultCachedDocument
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *


@pbot.on_message(filters.command('ban'))
async def ban(bot, update):
    me = await bot.get_me()
    BOT_ID = me.id
    try:
        if IsAdmin(update.from_user.id):
            if len(update.text.split()) != 3:
                await update.reply_text('You should try this format: /ban {user_id} {reason}')
            else:
                try:
                    parts = update.text.split()
                    user_id = parts[1]
                    reason = ' '.join(parts[2:])
                    rsn = f"{reason} : Banned By {update.from_user.first_name} [{update.from_user.id}]"
                    print(user_id + "_" + rsn)
                    ban_log_text = f"Banning user {user_id} for the reason {reason}."
                    try:
                        info = await bot.get_users(user_ids=user_id)
                        uname = info.username
                        name = info.first_name
                    except:
                        uname = "None"
                        name = id
                    Ban(rsn, user_id, uname)
                    try:
                        await bot.send_message(user_id, f"You are Banned From This Bot!\n\nReason: {reason}\nBanned By: {update.from_user.mention}",
                        reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('Request Unban', callback_data="banrq")
                        ]
                        ]
                        ))
                        ban_log_text += "\n\n✅ User notified successfully! ✅"
                    except Exception as e:
                        traceback.print_exc()
                        ban_log_text += f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
                    await update.reply_text(ban_log_text)
                    await bot.send_message(LOG_CHNL, ban_log_text)
                    await update.reply_text(f"User [{name}](tg://user?id={user_id}) Banned Successfully!")
                except Exception as e:
                    await SendLog(e, update.from_user.first_name, update.from_user.id, update.chat.id)
        else:
            await update.reply_text('Eww You are Not an Admin!')
    except Exception as e:
        await SendLog(e, update.from_user.first_name, update.from_user.id, update.chat.id)


@pbot.on_message(filters.command('unban'))
async def unban(bot, update):
    me = await bot.get_me() 
    BOT_ID = me.id
    try:
        if IsAdmin(update.from_user.id):
            if len(update.text.split()) != 2:
                await update.reply_text('You should try this format: /unban {user_id}')
            else:
                try:
                    parts = update.text.split()
                    user_id = parts[1]
                    unban_log_text = f"Unbanning user {user_id}"
                    await bot.get_users(user_ids=user_id)
                    UnBan(user_id)
                    try:
                        await bot.send_message(user_id, "Your ban was lifted!")
                        unban_log_text += "\n\n✅ User notified successfully! ✅"
                    except Exception as e:
                        traceback.print_exc()
                        unban_log_text += f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
                    await update.reply_text(unban_log_text)
                    await bot.send_message(LOG_CHNL, unban_log_text)
                except Exception as e:
                    await SendLog(e, update.from_user.first_name, update.from_user.id, update.chat.id)
        else:
            await update.reply_text('Eww You are Not an Admin!')
    except Exception as e:
        await SendLog(e, update.from_user.first_name, update.from_user.id, update.chat.id)


@tbot.on(events.NewMessage(pattern='/.*listbanned', from_users=GetAdminIdList()))
async def banlst(e):
    c = await e.get_chat()
    await ProcessingMsg(c.id, 0.5)
    Users = GetBanned()
    Data = '<b><u>🌷 Hᴇʀᴇ Is Dᴇᴛᴀɪʟs Oꜰ Banned Usᴇʀs Iɴ Dᴀᴛᴀʙᴀsᴇ...🌹</u></b>\n\n<b>Usᴇʀs:</b> <code>{}</code>'.format(
        len(Users))
    await tbot.send_message(c, Data, buttons=[[Button.inline('🌺 Gᴇɴᴇʀᴀᴛᴇ Lɪsᴛ 💐', data='genbuserlist')]], parse_mode='html')
