import discord
import logging
from discord.ext import commands
import os
import random


TOKEN = "OTUzOTgzMTE1MzAxMzc2MDUx.YjMgAg.-_cTYSWTueDFbUgkqqJRE8Y10g0"

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    userid = str(message.author.id)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "bot-spam":
        if userid == "612009487808724992" and user_message.lower() == "!hello":
            await message.channel.send(f"Grüss dich Sinjin Yilmaz Ramazan Erdogan Emrecan Süffelcan Ilhan Emre Sifcan Fischcan Sünjerle Münjerle Dünger Sinjan.")
            return
        else:
            if user_message.lower() == "!hello":
                await message.channel.send(f"Hello {username}!")
                return

    if message.channel.name == "bot-spam":
        if userid == "748618875180154980" and user_message.lower() == "!quit":
            await message.channel.send(f"Going back to grinding..") and await client.close()
            return

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

client.run(TOKEN)
