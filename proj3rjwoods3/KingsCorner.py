import random, sys
from KingsCornerBoard import KingsCornerBoard
from KingsCornerRules import KingsCornerRules
from Card import Card
from Field import Field
from Player import Player

class KingsCorner:

    numplayers = 0

    def getMoveFromPlayer(self):
        move = input("What will you do? (h for help): ")
        move = move.lower()

        return move

    def prepareTurn(self, board, rules, player):
        player.drawFromDeck(board.deck)
        rules.printBoard(board, player)

    def initPlayers(self):

        self.numplayers = 0
        while self.numplayers < 2 or self.numplayers > 4:
            self.numplayers = int(input("How many players? (2-4): "))
            if self.numplayers < 2 or self.numplayers > 4:
                print("Player number must be between 2 and 4")
        players = {}

        for p in range(self.numplayers):
            pname = input("Name of player {}?: ".format(p + 1))
            players.update( {p + 1 : Player(p + 1, pname) } )

        return players

    def __init__(self):

        rules = KingsCornerRules()

        # init players
        players = self.initPlayers()
        numplayers = self.numplayers
        # init deck
        deck = rules.createDeck()
        # create board
        board = KingsCornerBoard(deck, players, numplayers)

        # draw 7 cards each
        for p in range(numplayers):
            players[p + 1].newHand(deck)

        # play 1 card in each N,S,E,W
        board.initfields()

        winner = None
        # everything is set, now loop on turns and give rules per turn
        while winner == None:

            # go in turn order
            for p in range(numplayers):
                currentPlayer = players[p + 1]

                turnend = 0
                self.prepareTurn(board, rules, currentPlayer)
                while not turnend:

                    move = self.getMoveFromPlayer()

                    if move == 'end':
                        turnend = 1
                    elif move.startswith('play'):
                        rules.tryToPlay(currentPlayer, board, move)
                    elif move.startswith('move'):
                        rules.tryToMove(currentPlayer, move, board)
                    elif move.startswith('h'):
                        rules.printHelp()
                    else:
                        print('Invalid syntax. Type \'h\' for a list of moves')

                    winner = rules.determineIfPlayerHasWon(currentPlayer)
                    if winner != None:
                        break

                if winner != None:
                    break

                input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNEXT PLAYER, PRESS ENTER WHEN READY\n')

        #this means the game has ended
        print('Congrats %s, you win~' % winner)







