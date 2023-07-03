from telethon import events, Button
from alpha import tbot
from alpha.helpers.status import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@tbot.on(events.NewMessage(pattern="^[/]invitelink"))
async def invitelink(event):

    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return
    link = await tbot(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"Group link of {event.chat.title} is [here]({link.link})", link_preview=False)

