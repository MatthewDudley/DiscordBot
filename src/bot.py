# --- imports ---
from __future__ import print_function
import discord
from config import BOT_TOKEN
from discord.ext import commands, tasks
from itertools import cycle
import mlbgame
# --- imports end ---


# --- variables ---
bot = commands.Bot(command_prefix = '.')
status = cycle(['.help for commands', '.score', '.lineup', '.standings', '.info'])
# --- variables end ---


# --- bot envents ---
@bot.event
async def on_ready():
    
    # call change_status method for rotating status
    change_status.start()

    # gather relevent information for commands
    # ! This step is due to the mlbgame wrapper being really slow.
    # ! So I start getting the information as soon as the bot goes online and run every 12 hours. 
    # ! This should be enough for this bots functionality
    # ? I plan to improve this once I find a decent free real time api or mlb comes out with thier own :)

    # log bot is running
    print(f'{bot.user.name} is ready...\n')
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
    print(f'Pong! {round(bot.latency * 1000)}ms\n')
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

# # braves command
# @bot.command()
# async def braves(ctx):

# standings command
@bot.command()
async def standings(ctx):
    
    standings = mlbgame.standings()          
    
    header = str.format('{0:25} {1:5} {2:5} {3:6} {4:5}\n'.format('Team', 'W', 'L', 'L10', 'GB'))
    divider = '-------------------------------------------------\n'
    standings_txt = ''
    
    for division in standings.divisions:
        
        if (division.name == 'NL East'):            
        
            print('geting NL East stadnings...\n')
        
            for team in division.teams:
                standings_txt += str.format('{0:25} {1:<5} {2:<5} {3:<6} {4:<5}\n'.format(team.team_full, team.w, team.l, team.last_ten, team.gb))
        else:
            break

    # send message
    print(header + divider + standings_txt)
    await ctx.send(' ```' + header + divider + standings_txt + ' ```')

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