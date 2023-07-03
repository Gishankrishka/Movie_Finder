from pyrogram import filters ,Client
from pyrogram.errors import MessageEmpty
from alpha import pbot

@pbot.on_message(filters.group & filters.command('send'))
async def ban(bot, update):
    await update.delete()
    me=await bot.get_me()
    BOT_ID=me.id
    st= await bot.get_chat_member(update.chat.id, update.from_user.id)
    if st.privileges.can_restrict_members ==True:
        try:
            m=update.text
            msg=m.replace('/send' ,'')
            if update.reply_to_message:
                msg_id=update.reply_to_message_id
                await  bot.send_message(chat_id=update.chat.id , 
                text=msg,
                reply_to_message_id=msg_id)
            else:
                await bot.send_message(update.chat.id , msg)
        except MessageEmpty:
            pass
