import os
import random


TOKEN = "5015207309:AAEoifISfnyTYGGZkPLWnXpMQVGM7mEkGf8"
API_ID = 2919867
API_HASH = "90dd95178a8d13a69bfdbc7da68d23a4"
CHANNEL = -1001523814336
SUDO_USERS = set(int(x) for x in  [5073412581,1392459364,1242979521,1337239251,2043468602,1791795037])

SUBREDS = [
    "dankmemes",
    "Animememes",
    "memes",
    "meme",
    "memes_of_the_dank",
    "Wholesomeanimemes",
    "Weeaboo",
    "Narutomemes",
    "JojoMemes",
    "Onepiecememes",
    "Memepiece",
    "Mhamemes",
    "Lostpause",
    "AnimeFunny",
    "AnimeMirchi"
    "AnimeMeme",
    "AttackOnTitanmemes",
    "DankAnimeMemes",
    "EliteWeebs",
    "Anime_Memes",
    "AnimeAnimemes",
    "GreatestAnimeMemes",
    "insanepeoplefacebook",
    "Goodanimemes",
    "animemes",
    "dankindia"
]

subreddits = random.choice(SUBREDS)
API = f"https://meme-api.herokuapp.com/gimme/{subreddits}"
