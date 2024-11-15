from distutils.command.config import config
import traceback, os, io, re, asyncio
from telethon import events, Button
from pyrogram.errors import InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from alpha import tbot, pbot, aiohttpsession
from .db import *
from art import *
from var import *
from asyncio import gather
from io import BytesIO
from pyrogram import filters
from imdb import IMDb
from pyrogram.types import *
from pyrogram.errors import *
from asyncio import sleep


USER_NOT="""🚫 Access Denied
hey {} ,
you must join [Our Channell](https://t.me/AlphaTm_Botz).
so ,please join and try again 
"""
CHANNEL_LINK = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('💌 Channel 1 (First Join Here)', url='https://t.me/AlphaTm_Botz'),
            InlineKeyboardButton('💌 Channel 2 (And Join Here)', url='https://t.me/AlphaRedirecttoMain')
        ],
        [
            InlineKeyboardButton('🎡 Support Group', url='https://t.me/AlphaTm_Botz_chat')
        ],
        [
            InlineKeyboardButton('♻️ Refresh ♻️', callback_data='ref')
        ]
    ]
)
 

async def is_sub(bot, update):
        if not IsBan(update.from_user.id):    
            try:
                await bot.get_chat_member('AlphaRedirecttoMain', update.from_user.id)
            except UserNotParticipant:
                return await pbot.answer_inline_query(
                update.id,
                results=[],
                switch_pm_text="You have to subscribe channel",
                switch_pm_parameter="force",
                cache_time=0

                )
        else:
            return await pbot.answer_inline_query(
                update.id,
                results=[],
                switch_pm_text="You Are Banned From This Bot",
                switch_pm_parameter="ban",
                cache_time=0

                )
async def forcesub(bot, update):
        if not IsBan(update.from_user.id):     
            try:
                await bot.get_chat_member('AlphaRedirecttoMain', update.from_user.id)
            except UserNotParticipant: 
                r=""
                if len(update.text.split()) > 1:
                    text = (update.text.split(None, 1)[1]).lower()
                    if text == "force":
                        return
                    elif text == "help":
                        return
                    else:
                        m= await bot.send_message(update.from_user.id,
                        text=USER_NOT.format(update.from_user.mention),
                        reply_markup=CHANNEL_LINK,
                        disable_web_page_preview=True) 
                        await sleep(30)
                        await m.delete()
                        return(r)
                else:
                    m= await bot.send_message(update.from_user.id,
                    text=USER_NOT.format(update.from_user.mention),
                    reply_markup=CHANNEL_LINK,
                    disable_web_page_preview=True) 
                    await sleep(30)
                    await m.delete()
                    return(r)
        else:
            return await update.reply_text("You Are Banned From This Bot!")

async def In_MGps(Id):  
        Gps = GetmGrps()
        for Grps in Gps:
            if int(Grps)==Id:
                In_MGps = True     
                break
            else:
                In_MGps = False   
        return In_MGps

async def forcesub_cl(bot, update):
        try:
            await bot.get_chat_member('AlphaRedirecttoMain', update.from_user.id)
        except UserNotParticipant: 
            r=""
            m= await bot.send_message(update.from_user.id,
            text=USER_NOT.format(update.from_user.mention),
            reply_markup=CHANNEL_LINK,
            disable_web_page_preview=True) 
            await sleep(30)
            await m.delete()
            return(r)

LogChannel = LOG_CHNL

def IsAdmin(id):
    Admins = GetAdmins()
    for admin in Admins:
        if int(admin) == id:
            isAdmin = True
            break
        else:
            isAdmin = False
    return isAdmin

def IsBan(id):
    Ban = GetBanned()
    for user in Ban:
        if int(user) == id:
            isBan = True
            break
        else:
            isBan = False
    return isBan

def IsCommand(text):
    try:
        if text == None:
            return False
        elif text[0] == '/':
            return True
        else:
            return False
    except:
        return False

async def mention_html(name: str, user_id: int) -> str:
    name = escape(name)
    return f'<a href="tg://user?id={user_id}">{name}</a>'


async def mention_markdown(name: str, user_id: int) -> str:
    return f"[{(await escape_markdown(name))}](tg://user?id={user_id})"
  

import nltk

# Download NLTK data (if you haven't already)
nltk.download('words')

from nltk.corpus import words

# Get a list of English words
english_words = set(words.words())

def suggest_similar_word(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching
    if user_input in english_words:
        return
    suggestions = [word for word in english_words if word.startswith(user_input)]
    if suggestions:
        suggestion = suggestions[0]
        reply = f"Did you mean '{suggestion}'?"
    else:
        reply = False
    return reply


async def AddNewUser(UserName: str, ID: int):
    Added = GetUsers()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True
            break
        else:
            pass
    if IsAdded == False:
        AddUser(UserName, ID)
        msg = '💥 Nᴇᴡ Usᴇʀ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {}\n🌴 ID : {}\n🌴 Aʟʟ Usᴇʀs : {}'.format(
            '@{}'.format(UserName) if UserName != None else 'None', ID, len(Added))
        await tbot.send_message(LogChannel, msg)


async def AddNewGroup(Title: str, ID: int):
    Added = GetGrps()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True
        else:
            pass
    if IsAdded == False:
        Data.child(f'{ID}/')
        AddGroup(Title, ID)
        await tbot.send_message(LogChannel, f'💥 Nᴇᴡ Gʀᴏᴜᴘ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {Title}\n🌴 ID : {ID}\n🌴 Aʟʟ Gʀᴏᴜᴘs : {len(Added)}')


async def AddNewAdmin(UserName: str, ID: int):
    Added = GetAdmins()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True 
        else:
            pass
    if IsAdded == False:
        AddAdmin(UserName, ID)
        msg = '💥 Nᴇᴡ Aᴅᴍɪɴ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {}\n🌴 ID : {}\n🌴 Aʟʟ Aᴅᴍɪɴs : {}'.format('@{}'.format(UserName) if UserName != None else 'None', ID, len(Added))
        await tbot.send_message(LogChannel, msg)


        
async def RemSAdmin(UserName: str, ID: int):
        RemAdmin(int(ID))
        msg = '💥 Remove Admin From Database 💥\n🌴 UsᴇʀNᴀᴍᴇ : {}\n🌴 ID : {}'.format('@{}'.format(UserName) if UserName != None else 'None', ID)
        await tbot.send_message(LogChannel, msg)

async def ALLCast(from_chat_id, message_id, first_name, sender_id, forward=True):
    Groups = GetGrps()
    Users = GetUsers()
    await pbot.send_message(from_chat_id, f'🌴 BROΔDCΔSΓ SΓΔRΓED...! 🌹\n🌾 Sending This Post To **{len(Users)}** Users....🌻\n🌾 Sending This Post To **{len(Groups)}** Groups....🌻')
    SentGrp = 0
    SentUsr = 0
    for key in Users:
        try:
            if forward:
                await pbot.forward_messages(chat_id=int(key), from_chat_id=from_chat_id, message_ids=message_id)
            else:
                await pbot.copy_message(chat_id=int(key), from_chat_id=from_chat_id, message_id=message_id)
            SentUsr += 1
        except InputUserDeactivated:
            RemUser(int(key))
        except UserIsBlocked:
            RemUser(int(key))
        except PeerIdInvalid:
            RemUser(int(key))
        except Exception:
            await SendLog(traceback.format_exc(), first_name, sender_id, from_chat_id)
    for key in Groups:
        try:
            if forward:
                await pbot.forward_messages(chat_id=int(key), from_chat_id=from_chat_id, message_ids=message_id)
            else:
                await pbot.copy_message(chat_id=int(key), from_chat_id=from_chat_id, message_id=message_id)
            SentGrp += 1
        except InputUserDeactivated:
            RemUser(int(key))
        except UserIsBlocked:
            RemUser(int(key))
        except PeerIdInvalid:
            RemUser(int(key))
        except Exception:
            pass
    await pbot.send_message(from_chat_id, f'🌻 𝔖𝔢𝔫𝔡𝔦𝔫𝔤 𝔬𝔣 𝔱𝔥𝔢 𝔟𝔯𝔬𝔞𝔡𝔠𝔞𝔰𝔱 𝔭𝔬𝔰𝔱 𝔦𝔰 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔠𝔬𝔪𝔭𝔩𝔢𝔱𝔢𝔡! 🌺\nSent To ⚡️ {SentUsr} ⚡️ Users....🌷\nSent To ⚡️ {SentGrp} ⚡️ Groups....🌷')


async def SendLog(log, fname, id, chat):
    await tbot.send_message(LogChannel, f'🌷 Bot Crashed 🍇\n\nTo User ⚡️ [{fname}](tg://user?id={id})\nIn Chat ⚡️ `{chat}`\nError Log 🌴```{log}```')



def GetAdminIdList():
    Admins = GetAdmins()
    IDs = []
    for key in Admins:
        IDs.append(int(key))
    return IDs

async def ProcessingMsg(chat_id, time, delete=True):
    txt = ['Pʀᴏᴄᴇssɪɴɢ [ 🌼 ]', 'Pʀᴏᴄᴇssɪɴɢ [ 🌼 🌼 ]', 'Pʀᴏᴄᴇssɪɴɢ [ 🌼 🌼 🌼 ]']
    m = await tbot.send_message(chat_id, txt[0])
    time_one = round(time/3, 3)
    for x in range(1, 3):
        await asyncio.sleep(time_one)
        await tbot.edit_message(chat_id, m, txt[x])
    if delete:
        await asyncio.sleep(time_one)
        await tbot.delete_messages(chat_id, m)
    else:
        return m
def get_replied_file_details(message):
    try:
        # Check if the message has a replied file
        if message.reply_to_message and message.reply_to_message.document:
            # Get the Document object of the replied file
            document = message.reply_to_message.document

            # Retrieve the file details
            file_size = document.file_size
            duration = document.duration
            file_name = document.file_name
            file_id = document.file_id
            caption = message.caption

            # Return the file details
            return file_size, duration, file_name, file_id
    except Exception as e:
        SendLog(e, message.from_user.first_name, from_user.id, message.chat.id)
    return None

async def GetUsrsGrpsToTxt(chat):
    Users = GetUsers()
    Groups = GetGrps()
    FileName = 'UsrsAndGrps.txt'
    Data = 'Here Is A List Of Users In Database...\n\n'    
    for key, val in Users.items():
        Data = f'{Data}==> @{val}: {key}\n'
    Data = f'{Data}\n-----------------------------------------------------------------'
    Data = f'{Data}\n\nHere Is A List Of Groups In Database...\n\n'
    for key, val in Groups.items():
        Data = f'{Data}==> {val}: {key}\n'
    Data = f'{Data}\n-----------------------------------------------------------------'
    Data = f'{Data}\n\nAll Users: {len(Users)}\nAll Groups: {len(Groups)}'
    with io.open(FileName, 'w', encoding='utf-8') as f:
        f.write(Data)
    await tbot.send_message(chat, file=FileName, message='**🌷 Hᴇʀᴇ Is A Lɪsᴛ Oꜰ Usᴇʀs Iɴ Yᴏᴜʀ Dᴀᴛᴀʙᴀsᴇ 🌻**')
    os.remove(FileName)

async def GetBAnsToTxt(chat):
    Users = GetBanned()
    FileName = 'Banned.txt'
    Data = 'Here Is A List Of Banned Users In Database...\n\n'    
    for key, val in Users.items():
        Data = f'{Data}==> {key}: {val}\n'
    Data = f'{Data}\n-----------------------------------------------------------------'
    Data = f'{Data}\n\nAll Users: {len(Users)}'
    with io.open(FileName, 'w', encoding='utf-8') as f:
        f.write(Data)
    await tbot.send_message(chat, file=FileName, message='**🌷 Hᴇʀᴇ Is A Lɪsᴛ Oꜰ Usᴇʀs Iɴ Yᴏᴜʀ Dᴀᴛᴀʙᴀsᴇ 🌻**')
    os.remove(FileName)


def GetButtonText(m, d):
    try:
        k = m.reply_markup.inline_keyboard
    except:
        return
    for bs in k:
        for b in bs:
            if b.callback_data == d:
                return b.text


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.sender_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e           

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image          

from pyrogram import filters
from pyrogram.types import Message

def replace_invalid_characters(text):
    invalid_characters = ['$','#[',']','/','.','_']
    replacement_characters = [' ', ' ' , ' ', ' ', ' ' ,' ',' ']
    
    for i in range(len(invalid_characters)):
        text = text.replace(invalid_characters[i], replacement_characters[i])
    
    return text

async def allowed_chat_filter_fn(_, __, m: Message):
    return bool(m.chat and m.chat.type in {"channel", "supergroup"})
async def menfilter(_, __, m: Message):
    return bool(m.text in {"@"})

allowed_chat_filter = filters.create(allowed_chat_filter_fn)
men = filters.create(menfilter)

def bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])

def find_movie_thumbnail(movie_name):
    ia = IMDb()
    movies = ia.search_movie(movie_name)
    
    if movies:
        # Get the first movie from the search results
        movie = movies[0]
        ia.update(movie)

        if 'full-size cover url' in movie:
            thumbnail_url = movie['full-size cover url']
            return thumbnail_url
    
    return None
