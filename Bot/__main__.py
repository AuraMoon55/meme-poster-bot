import asyncio
import time
import requests as req
from pyrogram import Client, filters
from config import *
from demcor import sudo_users_only

bot = Client('bot',api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN)


@bot.on_message(filters.command('start'))
def main(client, message):
    text = f"~Shoo Shoo~ Go Away.\nI work for @Anime_Meme_Kingdom Only"
    message.reply_text(text=text)

@bot.on_message(filters.command('post'))
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
        await bot.send_photo(chat_id=CHANNEL, photo=meme, caption=f"#meme {title} \n \n @Anime_meme_kingdom")
        time.sleep(360)
        
bot.run()

If SUDO_USERS not None :
def moan()
    bot.send_message("@Villainevil_support", "Im alive to post memes")

if name == "__main__.py"
   moan()
