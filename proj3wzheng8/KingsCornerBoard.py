from Board import Board
from Field import Field
from Card import Card

class KingsCornerBoard(Board):

    """
        The only field shared by the two games is a deck
    """
    def __init__(self, deck, players, numberPlayers):
        self.deck = deck
        self.players = players
        self.numberPlayers = numberPlayers
        self.N = Field()
        self.S = Field()
        self.E = Field()
        self.W = Field()
        self.C1 = Field()
        self.C2 = Field()
        self.C3 = Field()
        self.C4 = Field()

        self.boardDic = {'n': self.N, 's': self.S, 'e': self.E, 'w': self.W, 'c1': self.C1, 'c2': self.C2, 'c3': self.C3, 'c4': self.C4}

    """
        Initializes empty field placeholders
    """
    def initfields(self):

        # we need some sort of placeholder card for empty stacks
        empty = Card(0, 'empty', 'empty')

        self.C1.top = empty
        self.C1.bot = empty

        self.C2.top = empty
        self.C2.bot = empty

        self.C3.top = empty
        self.C3.bot = empty

        self.C4.top = empty
        self.C4.bot = empty

        self.N.top = self.deck.pop()
        self.N.bot = self.N.top

        self.S.top = self.deck.pop()
        self.S.bot = self.S.top

        self.E.top = self.deck.pop()
        self.E.bot = self.E.top

        self.W.top = self.deck.pop()
        self.W.bot = self.W.top