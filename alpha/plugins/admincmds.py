from pyrogram import filters
from telethon import events
from var import *
from alpha.helpers.funcs import *
from alpha import tbot, pbot

@pbot.on_message(filters.command(["bpromo"]))
async def welcome(bot, message):
    sender = message.from_user
    chat = message.chat
    try:
        if IsAdmin(sender.id):
            if message.reply_to_message:
                reply = message.reply_to_message
                r_sender = reply.from_user
                UserName = r_sender.username 
                ID = r_sender.id
            else:
                text = message.text.split()
                user_id = text[1]
                info = await bot.get_users(user_id)
                UserName, ID = info.username, info.id
            await AddNewAdmin(str(UserName), int(ID))
            await bot.send_message(chat.id, '🌺 Promoted User {} As Admin... 🌷'.format('@{}'.format(UserName) if UserName != None else ID))
            
        else:
            pass
    except Exception as Error:
        await SendLog(Error, message.from_user.first_name, message.from_user.id, message.chat.id)

@pbot.on_message(filters.command(["bdemo"]))
async def debote(bot, message):
    sender = message.from_user
    chat = message.chat
    try:
        if IsAdmin(sender.id):
            if message.reply_to_message:
                reply = message.reply_to_message
                r_sender = reply.from_user
                UserName = r_sender.username 
                ID = r_sender.id
            else:
                text = message.text.split()
                user_id = text[1]
                info = await bot.get_users(user_id)
                UserName, ID = info.username, info.id
            await RemSAdmin(str(UserName), int(ID))
            await bot.send_message(chat.id, '🌺 User {} Removed From Database... 🌷'.format('@{}'.format(UserName) if UserName != None else ID))
            
        else:
            pass
    except Exception as Error:
        sender = message.from_user
        await SendLog(Error, sender.first_name, sender.id, chat.id)

		

@tbot.on(events.NewMessage(pattern='/.*broadcast'))
async def broadcast(e):
	c, s, r = await e.get_chat(), await e.get_sender(), await e.get_reply_message()
	if IsAdmin(s.id):
		await ALLCast(c.id, r.id, s.first_name, s.id)

@tbot.on(events.NewMessage(pattern='/.*count', from_users=GetAdminIdList()))
async def SendUserList(e):
    c = await e.get_chat()
    await ProcessingMsg(c.id, 0.5)
    Groups = GetGrps()
    Users = GetUsers()
    Movies = GetMvs()
    Data = '<b><u>🌷 Hᴇʀᴇ Is Dᴇᴛᴀɪʟs Oꜰ Usᴇʀs Aɴᴅ Gʀᴏᴜᴘs Iɴ Dᴀᴛᴀʙᴀsᴇ...🌹</u></b>\n\n<b>Usᴇʀs:</b> <code>{}</code>\n<b>Gʀᴏᴜᴘs:</b> <code>{}</code>\n<b>Aʟʟ:</b> <code>{}</code>\n<b>Aʟʟ Movies:</b> <code>{}</code>'.format(
        len(Users), len(Groups), len(Users) + len(Groups), len(Movies))
    await tbot.send_message(c, Data, buttons=[[Button.inline('🌺 Gᴇɴᴇʀᴀᴛᴇ Lɪsᴛ 💐', data='genuserlist')]], parse_mode='html')
