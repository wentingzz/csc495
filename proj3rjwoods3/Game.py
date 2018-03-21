import sys
from bartok import bartok
from kingscorner import kingscorner
from enum import Enum

class Game():
    # BARTOK = 0,
    # KC = 1
    def __init__(self, gameType):
        self.game = gameType
        # self.deck
        # self.player
        # self.players
    def start(self):
        gameType() #pass in self which will have players/deck/board stuff

print("Start")
gameChoice = int(input("Which game would you like to play?\n0 - Bartok\n1 - Kings Corner\n> "))
gametype = None
if gameChoice == 0:
    print("You chose Bartok")
    gameType = bartok
elif gameChoice == 1:
    print("You chose Kings Corner")
    gameType = kingscorner
else:
    sys.exit("Invalid game selected")

game = Game(gameChoice);
game.start() #This can be a FSM that switches between player turns