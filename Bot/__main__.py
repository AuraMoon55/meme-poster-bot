import asyncio
import time
import requests as req
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import *
from demcor import sudo_users_only

bot = Client('bot',api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN)


@bot.on_message(filters.command['start', 'start@VGW_bot'])
def main(client, message):
    text = f"Hey there {message.from_user.id}, I am meme poster bot which uploads memes from reddit.\nI work for @Anime_Meme_Kingdom Only"
    buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Meme Channel", url = "t.me/Anime_Meme_Kingdom"
            ),
            InlineKeyboardButton(
                text="FAQs", callback_data="faqsinline"
            ),
        ],
    ]
)
    message.reply_text(text=text, reply_markup=buttons)

@bot.on_callback_query(filters.regex("faqsinline"))
async def faqs(_, query):
    texto = """ Im just a nub bot made by @Villainevil_Support"""
    await query.message.edit(text=texto)

@bot.on_message(filters.command['post', 'post@VGW_bot'], filters.user(SUDO_USERS))
@sudo_users_only
async def post(_, message):
    while True:
        x = req.get(API)
        if x.status_code != 200:
            return
        else:
            x = x.json()
        title=x.get(str("title"))
        meme=x.get(str("url"))
        await bot.send_photo(chat_id=CHANNEL, photo=meme, caption=f"#offtopic #meme {title} \n \n @Anime_meme_kingdom")
        time.sleep(10)

@bot.on_message(filters.command['post_here', 'post_here@VGW_bot'], filters.user(SUDO_USERS))
@sudo_users_only
async def post(_, message):
    while True:
        x = req.get(API)
        if x.status_code != 200:
            return
        else:
            x = x.json()
        title=x.get(str("title"))
        meme=x.get(str("url"))
        await bot.reply_photo(chat_id=message.from_user.id, photo=meme, caption=f"#offtopic #meme {title} \n \n @Anime_meme_kingdom")
        time.sleep(10)
        
bot.run()

def moan():
    bot.send_message("@Villainevil_support", "Im alive to post memes")

if __name__ == "__main__":
   moan()
