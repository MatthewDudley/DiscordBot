from __future__ import print_function
import mlbgame

print('in braves command')
month = mlbgame.games(2015, 6, home='Mets')
games = mlbgame.combine_games(month)
print(games[0])