import os
import json
import random

def get_user_list(config, key):
    with open("{}".format(config), "r") as json_file:
        return json.load(json_file)[key]

SUMDOS = get_user_list("sum.json", "sumdo")

TOKEN = "5015207309:AAE1Hf1L1zpJ-YNxNcbP0AooJwu29DT-0So"
API_ID = 2919867
API_HASH = "90dd95178a8d13a69bfdbc7da68d23a4"
CHANNEL = -1001523814336
SUDO_USERS = set(int(x) for x in  SUMDOS)

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
