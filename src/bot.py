# --- imports ---
import discord
from config import BOT_TOKEN
from discord.ext import commands, tasks
from itertools import cycle
# --- imports end ---


# --- variables ---
bot = commands.Bot(command_prefix = '.')
status = cycle(['.help for commands', '.score [team]', '.lineup [team]', '.standings', '.games'])
# --- variables end ---


# --- bot envents ---
@bot.event
async def on_ready():
    # call change_status method for rotating status
    change_status.start()
    # log bot is running
    print(f'{bot.user.name} is ready...')
# --- bot events end ---


# --- task for rotating status ---
@tasks.loop(seconds = 5) # run ever 5 seconds
async def change_status():
    # change status
    await bot.change_presence(activity=discord.Game(next(status)))
# --- task end ---


# --- bot commands ---
## help command


## ping command
@bot.command()
async def ping(ctx):
    # log pong message
    print(f'Pong! {round(bot.latency * 1000)}ms')
    # send pong message to the channel
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

## change prefix command
@bot.command()
async def prefix(ctx, newPrefix):
    # save previos prefix for logging and retured message
    prevPrefix = bot.command_prefix
    # log change
    print(f'Changing prefix command from {prevPrefix} to {newPrefix}')
    # change the prefix
    bot.command_prefix = newPrefix
    # send message indicating new prefix
    await ctx.send(f'New command prefix is {bot.command_prefix}!')

# dev | stop command
@bot.command()
async def stop(ctx):
    # log got is going offline
    print(f'{bot.user.name} is going offline')
    # logout bot
    await bot.logout()
# --- bot commands end ---


# --- run bot ---
try:
    bot.run(BOT_TOKEN)
except:
    print('ERROR - error occured at bot.run')
# --- run bot end ---