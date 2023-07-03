from datetime import datetime
from alpha import pbot
from pyrogram import filters ,Client


@pbot.on_message(filters.command("ping") )
async def _ping(bot, update):
    start = datetime.now()
    replied = await update.reply('`procesing....`')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await replied.edit(f"**Pong!**\n`{m_s} ms`")
