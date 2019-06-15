import discord
from discord.ext import commands
from config import BOT_TOKEN

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready...')

client.run(BOT_TOKEN)