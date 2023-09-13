from pyrogram.types import InlineQueryResultCachedDocument, InlineQueryResultArticle, InputTextMessageContent
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import *
from alpha import pbot, tbot
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha.__version__ import __version__, __license__, __copyright__ 

@pbot.on_inline_query()
async def answer(client, inline_query):
    if inline_query.query == 'bshare':
       	await inline_query.answer(
            results=[
                InlineQueryResultPhoto(
                    title="Share Karapam",
                    photo_url="https://telegra.ph/file/a1d57aa7a5c4f0401667b.jpg",
                    caption=f"""
**🎬 Discover an extraordinary film experience with our Telegram bot! Forget about ordinary Telegram channels because now you can access thousands of films using our film bot. 🎥🤖

📌 How to Use:
__1️⃣ Start the bot with the button under the post.
2️⃣ Join To Force Sub Chanes.
3️⃣ Give your movie name to the bot, and it will show you a list of movies you want. Then select the quality you want for the movie.
4️⃣ You can also use the bot inline. 🍀__

📌 Features:
__✅ Enjoy the bot's inline search for films in various qualities.
✅ Browse through our extensive collection of 10,000+ films.
✅ User-friendly interface for easy navigation.__

💭 Experience the convenience of our bot here:
👉 __@Alpha_movie_finder_bot__

🤦‍♀️__If you have any questions, feel free to ask at @AlphaTm_Botz_chat.__

Alpha Movie Finder v2
©Bot From[ 𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』 ](https://t.me/AlphaTm_Botz)

**Post by**: __{inline_query.from_user.mention}__**
""",
                    reply_markup=InlineKeyboardMarkup([[              
                        InlineKeyboardButton(' 𝙰𝙻𝙿𝙷𝙰 么 ™  Movie Finder', user_id="Alpha_movie_finder_bot")
                    ],
                    [
                        InlineKeyboardButton('Update Channel', url="http://t.me/AlphaTm_Botz"),
                        InlineKeyboardButton('Support Group', url="http://t.me/AlphaTm_Botz_chat")
                    ],
                    [
                        InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么️", url="https://t.me/+jrqciS7XvKNhODc1")
                    ]])
                ),
            ],
            cache_time=1
        )
    else:    
        await is_sub(client, inline_query)     
        query = inline_query.query.lower()
        q_id = inline_query.id
        results = []

        data = GetMvs()  # Retrieve data from the database

        count = 0  # Counter for limiting the number of results
        for key, val in data.items():
            movie_title = replace_invalid_characters(val.get("Title", ""))
            nm = movie_title.lower()
            if query in nm:
                movie_title = val.get("Title", "")
                kb = int(val.get("Size", ""))
                inkb = kb / 1048576
                movie_size = "{:.2f}".format(inkb)
                movie_caption = val.get("Caption", "")
                file_id = val.get("FileId", "")
                caption = f"Name: `{movie_title}`\nSize: `{movie_size} MB`\nCaption: `{movie_caption}`"
                url=f"http://t.me/Alpha_movie_finder_bot?start={key}"     
                result = InlineQueryResultCachedDocument(
                    title=movie_title,
                    document_file_id=file_id,
                    description="",
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup([
                        [              
                            InlineKeyboardButton('Inline Here', switch_inline_query_current_chat=""),
                            InlineKeyboardButton('Inline Another Chat', switch_inline_query=""),
                        ],
                        [ 
                            InlineKeyboardButton('Shareable Link 🔗', url=url),        
                            InlineKeyboardButton("Share Link",url=f'https://t.me/share/url?url={url}')            
                        ],
                        [
                            InlineKeyboardButton('🌝 Share Us 🌝', switch_inline_query="bshare"),
                        ],
                        [
                            InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="https://t.me/+jrqciS7XvKNhODc1")
                        ]
                    ])
                )

                results.append(result)
                count += 1

                if count == 30:  # Limit the number of results to 10
                    break
        switch_pm_text = 'Newest Updates'
        if count == 0:  # No results found
            suggestion = suggest_similar_word(query)
            switch_pm_text = 'No results found.'
            if suggestion:
                no_results_content = InputTextMessageContent(suggestion)
                no_results_result = InlineQueryResultArticle(
                    title=suggestion,
                    input_message_content=no_results_content
                ) 
            else:    
                no_results_content = InputTextMessageContent("No results found.")
                no_results_result = InlineQueryResultArticle(
                    title="No Results",
                    input_message_content=no_results_content
                )
            results.append(no_results_result)

        await pbot.answer_inline_query(
            q_id,
            results,
            switch_pm_text=switch_pm_text,
            switch_pm_parameter="inlinest",
            cache_time=0
        )
