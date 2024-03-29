import discord
from discord.ext import commands

TOKEN = "OTUzOTgzMTE1MzAxMzc2MDUx.YjMgAg.-_cTYSWTueDFbUgkqqJRE8Y10g0"

client = discord.Client()
bot = commands.Bot(command_prefix="+")

bot.lavalink_nodes = [
    {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
]


@bot.event
async def on_ready():
    print("Logged in as", bot.user.name)


@bot.command(aliases=["quit"])
@commands.has_any_role("Developer", 748618875180154980)
async def close(ctx):
    await bot.close()
    print("Bot Closed")
    exit()


@bot.command(pass_context=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)


@bot.command()
async def krapfen(ctx):
    await ctx.send(f"Berliner > Krapfen")


@bot.command()
async def hello(ctx):
    if (
        ctx.channel.id == 953990615018913802
        and ctx.message.author.id == "612009487808724992"
    ):
        await ctx.send(
            "Grüss dich Sinjin Yilmaz Ramazan Erdogan Emrecan Süffelcan Ilhan Emre Sifcan Fischcan Sünjerle Münjerle Dünger Sinjan."
        )
    else:
        await ctx.send(f"Hello {ctx.message.author.mention}!")


@bot.command()
async def punch(ctx, arg):
    if ctx.channel.id == 953990615018913802:
        await ctx.send(f"Punched {arg}")


@bot.command()
async def info(ctx):
    if ctx.channel.id == 953990615018913802:
        await ctx.send(ctx.guild)
        await ctx.send(ctx.author)
        await ctx.send(ctx.message.id)


bot.load_extension("dismusic")
bot.run(TOKEN)
