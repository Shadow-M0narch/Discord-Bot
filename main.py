import discord
from discord.ext import commands
import command
import logging


TOKEN = "OTUzOTgzMTE1MzAxMzc2MDUx.YjMgAg.-_cTYSWTueDFbUgkqqJRE8Y10g0"

client = discord.Client()
bot = commands.Bot(command_prefix="+")


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


logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

client.run(TOKEN)
