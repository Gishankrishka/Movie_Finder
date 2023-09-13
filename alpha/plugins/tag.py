from pyrogram import filters
from pyrogram.types import Message
from asyncio import sleep
import os
from alpha import pbot, tbot
from pyrogram.errors import FloodWait,UserAdminInvalid
from alpha.helpers.funcs import *
from cachetools import TTLCache
import os, logging, asyncio
from telegraph import upload_file
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import Client, filters
from pyrogram.types import Message

@pbot.on_message(filters.regex('@admin') & filters.command('tagadmin', 'tagadmins'))
async def tag_admins(c: Client, m: Message):

    adminslist = []

    if m.chat.type in ("supergroup", "group"):
        async for member in c.iter_chat_members(m.chat.id, filter="administrators"):
            adminslist.append(member.user.id)

        if m.from_user.id in adminslist:
            # Don't work if called by an admin himself and log this!
            pbot.send_message(LOG_CHNL,
                f"Called by admin: {m.from_user.name} ({m.from_user.id}) in Chat: {m.chat.title} ({m.chat.id})"
            )
            return

        mentions = "Hey **{}** Admins, look here!"
        admin_count = 0

        async for a in alladmins:
            if a.user.is_bot:
                pass
            else:
                admin_count += 1
                adminid = a.user.id
                mentions += f"[\u2063](tg://user?id={adminid})"

        text = mentions.format(admin_count)
        text += f"\n[{m.from_user.first_name}](tg://user?id={m.from_user.id}) is calling you!"
        await m.reply_text(text, parse_mode="markdown")

    else:
        await m.reply_text(
            "`It doesn't work here ¯\_(ツ)_/¯`",
            parse_mode="markdown",
            reply_to_message_id=m.message.id,
        )

    return

@tbot.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("Use This In Channel or Group!")
  
  admins = []
  async for admin in aditya.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Only Admin can use it.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("I can't Mention Members for Old Post!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Give me can an Argument. Ex: `/tag Hey, Where are you`")
  else:
    return await event.respond("Reply to Message or Give Some Text To Mention!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in aditya.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await aditya.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

# Cancle 

@tbot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in moment_worker:
    return await event.respond('__There is no proccess on going...__')
  else:
    try:
      moment_worker.remove(event.chat_id)
    except:
      pass
    return await event.respond('**__Stoped__**\n\n**__Powered By:__ @AdityaServer**')
