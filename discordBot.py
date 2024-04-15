import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from riot_api import main

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">>", intents=intents)

    
@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def bilans(ctx):
    chanel = bot.get_channel(int(os.getenv("ID_CHANNEL")))
    bilans = main()
    await chanel.edit(name=f"Winki: {bilans[0]} Luski: {bilans[1]}")
    await ctx.message.delete()
    await ctx.send(f"Mising wycarował {bilans[0]} razy!\n a 1lucky strolował {bilans[1]} razy!")

bot.run(os.getenv("DISCORD_TOKEN"))
