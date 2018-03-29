import random, sys
from KingsCornerBoard import KingsCornerBoard
from KingsCornerRules import KingsCornerRules
from Card import Card
from Field import Field
from Machine import Machine
from Player import Player, KingsAIPlayer

class KingsCorner:

    numplayers = 0

    # def prepareTurn(self, board, rules, player):
    #     player.drawFromDeck(board.deck)
    #     rules.printBoard(board, player)

    def initPlayers(self):
        self.numplayers = 0
        while self.numplayers < 1 or self.numplayers > 4:
            self.numplayers = int(input("How many players? (1-4): "))
            if self.numplayers < 1 or self.numplayers > 4:
                print("Player number must be between 1 and 4")
        players = {}

        if self.numplayers == 1:
            players.update({2: KingsAIPlayer(2, "AI")})
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

        if self.numplayers == 1:
            numplayers = numplayers + 1

        # create board
        board = KingsCornerBoard(deck, players, numplayers)
        # draw 7 cards each
        for p in range(numplayers):
            players[p + 1].newHand(deck)

        # play 1 card in each N,S,E,W
        board.initfields()

        # everything is set, now loop on turns and give rules per turn
        kMachine = Machine("KingsCorner", rules, players, numplayers, deck, board)
        kMachine.addState("end", "EndTurn", rules.endTurn)
        kMachine.addState("move", "Move", rules.tryToMove)
        kMachine.addState("play", "Play", rules.tryToPlay)
        kMachine.addState("h", "Help", rules.printHelp)
        kMachine.Kstart()
        kMachine.run()