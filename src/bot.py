# --- imports ---
import discord
from config import BOT_TOKEN
from discord.ext import commands, tasks
from itertools import cycle
# --- imports end ---

# --- variables ---
bot = commands.Bot(command_prefix = '.')
# --- variables end ---

# --- bot envents ---
@bot.event
async def on_ready():
    # set bot status and activity (Playing game)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('.bot for commands'))
    # log bot is running
    print(f'{bot.name} is ready...')
    
# --- bot events end ---

# --- bot commands ---
@bot.command()
async def ping(ctx):
    print(f'Pong! {round(bot.latency * 1000)}ms')
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# dev | stop running the bot
@bot.command()
async def stop(ctx):
    print('Bot is going offline')
    await bot.logout()
# --- bot commands end ---


# --- troll ---

# --- troll end ---

    


# --- run bot ---
try:
    bot.run(BOT_TOKEN)
except:
    print('[!]ERROR - bot.run')
    sys.exit(-1)
# --- run bot end ---