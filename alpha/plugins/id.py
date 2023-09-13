from pyrogram import filters ,Client
from alpha import pbot

@pbot.on_message( filters.command('id'))
async def id(bot, update):
    chat_id=update.chat.id
    if update.reply_to_message:
        msg_id=update.reply_to_message_id
        user_id=update.reply_to_message.from_user.id
        await update.reply_text(f"User ID: `{user_id}`\nChat ID: `{chat_id}`\nmsg ID: `{msg_id}`")
    elif len(update.command) == 1:
        await update.reply_text(
        f"Chat ID: `{chat_id}`\nMsg ID: `{update.id}`")
    else:
        u = update.command[1]
        user=await bot.get_users(u)
        await update.reply_text(f"User ID : `{user.id}`")
