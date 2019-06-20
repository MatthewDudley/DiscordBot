'''
    # ! This file is me testing out the mlbgame wrapper to see how calls work
    # ! Code in this file may not reflect the actual code used in the bot
'''

from __future__ import print_function
import mlbgame
from datetime import datetime

# ! current game or game by specific date
''' print('in braves command')
month = mlbgame.games(2019, 6, home='Braves')
print('month call complete\n')
games = mlbgame.combine_games(month)
print(f'game score: {games[len(games)-1]}\n')
gameID = games[len(games)-1].game_id
print(f'game id: {gameID}\n')
boxScore= mlbgame.box_score(gameID)
print(f'boxScore: {boxScore}\n')
print(boxScore.print_scoreboard()) '''

# ! NL East standings
standings = mlbgame.standings()
for division in standings.divisions:
    print()
    if (division.name == 'NL East'):
        print ("{0:25} {1:6} {2:6} {3:6}".format("Team", "W", "L", "L10"))
        print('--------------------------------------------')
        for team in division.teams:
            print ('{0:25} {1:<6} {2:<6} {3:<6}'.format(team.team_full, team.w, team.l, team.last_ten))

