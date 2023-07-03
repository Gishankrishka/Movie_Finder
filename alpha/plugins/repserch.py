from pyrogram.types import InlineQueryResultCachedDocument
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__
import re




@pbot.on_message(filters.incoming & filters.text)
async def repsech(bot, message):
    chat_ids = [key for key, value in MGroups.get().items()]
    if str(message.chat.id).startswith("-"):
        if str(message.chat.id) in str(MGroups.get().items()):  
            if message.text.startswith('/'):
                return
            movie_name = message.text
            thumbnail_url = 'https://telegra.ph/file/a1d57aa7a5c4f0401667b.jpg'
            buttons = []
            default_buttons = [
                InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』', url='https://t.me/AlphaTm_Botz'),
                InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 Botz Chat [#NoUB]', url='https://t.me/AlphaTm_Botz_chat')
            ]

            # Retrieve data from the database
            data = GetMvs()
            found_results = False  # Flag to track if any results were found
            reply_text = f"`{movie_name}`\n\n"
            count = 0
            for key, val in data.items():
                if len(movie_name) != 1:
                    movie_title = replace_invalid_characters(val.get("Title", ""))
                    nm = movie_title.lower()
                    text = nm
                    words = movie_name.lower().split()
                    # Construct the regular expression pattern dynamically based on user's words
                    pattern = r'\b{}\b'.format('.*'.join(words))
                    match = re.search(pattern, text)
                    if movie_name.lower() in nm:
                        found_results = True
                        movie_title = val.get("Title", "")
                        kb = int(val.get("Size", ""))
                        movie_size = kb / 1048576
                        movie_caption = val.get("Caption", "")
                        file_id = val.get("FileId", "")
                        caption = f"{movie_title}`\n\nSize: {movie_size}Mb`\nCaption: {movie_caption}"
                        button = InlineKeyboardButton(movie_title, callback_data=f'select_movie:{key}')
                        buttons.append([button])
                        count += 1

                        if count == 30:  # Limit the number of results to 10
                            await message.reply_text('Are You Looking For A TV series??', 
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton("Yes", callback_data="tsinfo")
                            ],
                                [
                                    InlineKeyboardButton("No", callback_data="notvs")
                                ],
                                [
                                    InlineKeyboardButton("Request 👤", callback_data="requ")
                                ]
                            ]
                            ))
                            return
            if found_results:
                reply_markup = InlineKeyboardMarkup(buttons + [default_buttons])
                await message.reply_photo(thumbnail_url, caption=reply_text + "Please select an option:", reply_markup=reply_markup)
            else:
                mm = message.text.replace(' ', '%20')
                suggestion = suggest_similar_word(message.text)
                if suggestion:
                    await message.reply_text(
                        text=f"**{suggestion}\nThen Copy And Send it\n\nIs Not? Check Spelling On [Google](https://www.google.com/search?q={mm})\n\n**Use the command `/remme {message.chat.id}` to stop sending movies**",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("Request 👤", callback_data="requ")
                        ],
                            [
                                InlineKeyboardButton("Search On Google 🌐", url=f"https://google.com/search?q={mm}/movie")
                            ],
                            [
                                InlineKeyboardButton("Click Here To Find Release Data 📅",
                                                     url=f"http://www.google.com/search?q={mm}%20movie%20Release%20Date")
                            ]
                        ]
                        ))
                else:
                    await message.reply_text(
                        text=f"**No Results Found In Our Database\nCheck Spelling On [Google](https://www.google.com/search?q={mm})\n\n**Use the command `/remme {message.chat.id}` to stop sending movies**",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("Request 👤", callback_data="requ")
                        ],
                            [
                                InlineKeyboardButton("Search On Google 🌐", url=f"https://google.com/search?q={mm}/movie")
                            ],
                            [
                                InlineKeyboardButton("Click Here To Find Release Data 📅",
                                                     url=f"http://www.google.com/search?q={mm}%20movie%20Release%20Date")
                            ]
                        ]
                        ))
    else:
        if await forcesub(bot, message):
            return
        if message.text.startswith('/'):
            return
        movie_name = message.text
        thumbnail_url = 'https://telegra.ph/file/a1d57aa7a5c4f0401667b.jpg'
        buttons = []
        default_buttons = [
            InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』', url='https://t.me/AlphaTm_Botz'),
            InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 Botz Chat [#NoUB]', url='https://t.me/AlphaTm_Botz_chat')
        ]

            # Retrieve data from the database
        data = GetMvs()
        found_results = False  # Flag to track if any results were found
        reply_text = f"`{movie_name}`\n\n"
        count = 0
        for key, val in data.items():
            if len(movie_name) != 1:
                movie_title = replace_invalid_characters(val.get("Title", ""))
                nm = movie_title.lower()
                if movie_name.lower() in nm:
                    found_results = True
                    movie_title = val.get("Title", "")
                    kb = int(val.get("Size", ""))
                    movie_size = kb / 1048576
                    movie_caption = val.get("Caption", "")
                    file_id = val.get("FileId", "")
                    caption = f"{movie_title}`\n\nSize: {movie_size}Mb`\nCaption: {movie_caption}"
                    button = InlineKeyboardButton(movie_title, callback_data=f'select_movie:{key}')
                    buttons.append([button])
                    count += 1

                    if count == 30:  # Limit the number of results to 10
                        await message.reply_text('Are You Looking For A TV series??', 
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("Yes", callback_data="tsinfo")
                        ],
                            [
                                InlineKeyboardButton("No", callback_data="notvs")
                            ],
                            [
                                InlineKeyboardButton("Request 👤", callback_data="requ")
                            ]
                        ]
                        ))
                        return
        if found_results:
            reply_markup = InlineKeyboardMarkup(buttons + [default_buttons])
            await message.reply_photo(thumbnail_url, caption=reply_text + "Please select an option:", reply_markup=reply_markup)
        else:
            mm = message.text.replace(' ', '%20')
            suggestion = suggest_similar_word(message.text)
            if suggestion:
                await message.reply_text(
                    text=f"**{suggestion}\nThen Copy And Send it\n\nIs Not? Check Spelling On [Google](https://www.google.com/search?q={mm})",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("Request 👤", callback_data="requ")
                    ],
                        [
                            InlineKeyboardButton("Search On Google 🌐", url=f"https://google.com/search?q={mm}/movie")
                        ],
                        [
                            InlineKeyboardButton("Click Here To Find Release Data 📅",
                                                 url=f"http://www.google.com/search?q={mm}%20movie%20Release%20Date")
                        ]
                    ]
                    ))
            else:
                await message.reply_text(
                    text=f"**No Results Found In Our Database\nCheck Spelling On [Google](https://www.google.com/search?q={mm})",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("Request 👤", callback_data="requ")
                    ],
                        [
                            InlineKeyboardButton("Search On Google 🌐", url=f"https://google.com/search?q={mm}/movie")
                        ],
                        [
                            InlineKeyboardButton("Click Here To Find Release Data 📅",
                                                 url=f"http://www.google.com/search?q={mm}%20movie%20Release%20Date")
                        ]
                    ]
                    ))


