import os
import random

TOKEN = os.environ.get('TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
CHANNEL = -1001523814336

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
    "animemes"
]

subreddits = random.choice(SUBREDS)
API = f"https://meme-api.herokuapp.com/gimme/{subreddits}"
