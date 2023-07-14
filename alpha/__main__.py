from pyrogram import idle
from var import *
from alpha import tbot, pbot
from os import listdir
from os.path import isfile, join
import importlib
from alpha.__version__ import __version__, __copyright__


mypath = 'alpha/plugins'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
Files = []
for file in onlyfiles:
	if file.split('.')[-1] == 'py':
		Files.append(file)
	else:
		pass
Imported = []
for file in Files:
    Imported.append(importlib.import_module(
    	'alpha.plugins.{}'.format(file.split('.')[0])))

async def log():
    if LOG_CHNL:
       await pbot.send_message(LOG_CHNL, BOT_STARTED.format(__version__, __copyright__))

pbot.start()
pbot.run(log())
tbot.start(bot_token=BOT_TOKEN)
print(BOT_STARTED.format(__version__, __copyright__))
idle()
