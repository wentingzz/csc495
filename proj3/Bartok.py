import random, sys, select

from BartokBoard import BartokBoard
from BartokRules import BartokRules
from Card import Card
from Field import Field
from Machine import Machine
from Player import Player, BartokAIPlayer

class Bartok:

    numplayers = 0

    def initPlayers(self):

        self.numplayers = 0
        while self.numplayers < 1 or self.numplayers > 4:
            self.numplayers = int(input("How many players? (1-4): "))
            if self.numplayers < 1 or self.numplayers > 4:
                print("Player number must be between 1 and 4")
        players = {}

        if self.numplayers == 1:
            players.update({2: BartokAIPlayer(2, "AI")})
        for p in range(self.numplayers):
            pname = input("Name of player {}?: ".format(p + 1))
            players.update( {p + 1 : Player(p + 1, pname) } )
        return players

    def __init__(self):
        rules = BartokRules()

        # init players
        players = self.initPlayers()
        numplayers = self.numplayers
        # init deck
        deck = rules.createDeck()

        if self.numplayers == 1:
            numplayers = numplayers + 1

        #create board
        board = BartokBoard(deck, players, numplayers)
        # draw 7 cards each
        for p in range(numplayers):
            players[p + 1].newHand(deck)

        # initialize the bartok state machine and run until someone wins
        bMachine = Machine("Bartok", rules, players, numplayers, deck, board)
        bMachine.addState("draw", "Draw", rules.drawCardAndEndTurn)
        bMachine.addState("play", "Play", rules.tryToPlay)
        bMachine.addState("h", "Help", rules.printHelp)
        bMachine.Bstart()
        bMachine.run()