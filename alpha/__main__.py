from pyrogram import idle
from var import *
from alpha import tbot, pbot
from os import listdir
from os.path import isfile, join
import importlib
from alpha.__version__ import __version__, __copyright__


def import_plugins():
    mypath = 'alpha/plugins'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    plugins = []

    for file in onlyfiles:
        if file.endswith('.py'):
            plugin_name = file.split('.')[0]
            module_path = f'alpha.plugins.{plugin_name}'
            try:
                plugin_module = importlib.import_module(module_path)
                plugins.append(plugin_module)
                print(f"Imported plugin: {plugin_name}")
            except Exception as e:
                print(f"Failed to import plugin: {plugin_name}")
                print(f"Error: {e}")

    return plugins


async def log():
    if LOG_CHNL:
        try:
            await pbot.send_message(LOG_CHNL, BOT_STARTED.format(__version__, __copyright__))
            print("Log message sent successfully.")
        except Exception as e:
            print(f"Failed to send log message: {e}")


def start_bots():
    try:
        pbot.start()
        pbot.loop.run_until_complete(log())
        print("pbot started successfully.")
    except Exception as e:
        print(f"Failed to start pbot: {e}")

    try:
        tbot.start(bot_token=BOT_TOKEN)
        print("tbot started successfully.")
    except Exception as e:
        print(f"Failed to start tbot: {e}")


if __name__ == "__main__":
    plugins = import_plugins()

    try:
        start_bots()
    except KeyboardInterrupt:
        pass

    idle()
