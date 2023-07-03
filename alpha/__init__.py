import aiohttp
from pyrogram import Client
from var import *
from telethon import TelegramClient
from pyromod import listen
import alpha.__version__
from alpha.__version__ import __copyright__ as cr

__version__ = __version__.__version__
__copyright__ = cr

pbot = Client("Alpha-Pyrogram", bot_token=BOT_TOKEN,
             api_hash=API_HASH, api_id=API_ID,)
tbot = TelegramClient("Alpha-Telethon", api_id=API_ID, api_hash=API_HASH)
aiohttpsession = aiohttp.ClientSession()
