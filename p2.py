import random, sys


class Card:
    def __init__(self, val, suit, color):
        # card number 0-10,J,Q,K
        self.val = val
        # card suit d = diamond, h = heart, c = club, s = spade
        self.suit = suit
        # extra color field because king's corner doesn't care about suit specifically (b or r)
        self.color = color

    def __repr__(self):
        print("Card value: " + str(self.val))
        print("Card suit: " + self.suit)
        print("Card color: " + self.color)
        print()
class Player:
    def __init__(self, num, name):
        # num = player number
        self.num = num
        # name = player name
        self.name = name
        # hand is the cards in the players hand
        self.hand = []
        # cc is the card count
        self.cc = 0
        # plan to use .active to determine the current turn
        self.active = False
        # .next on a player as a link to the next players turn maybe?
        self.next = self

    def draw(self, d):
        self.hand.append(d.pop())
        self.cc += 1

    def newhand(self, d, repeat = 7):
        for i in range(0, repeat):
            self.draw(d)

    def play(self, index):
        if index >= self.cc:
            print("Error: Trying to play a card out of index of the players hand")
            sys.exit()
        # this is broken ***********************************
        return self.hand.pop([index])


class Field:
    # A field is a playable location for cards (N is a field, a corner is a field)
    def __init__(self):
        # Using 0 as the representation of an empty field
        self.top = 0
        self.bot = 0




class Board:
    # A board is made of a deck and field for playing cards
    def __init__(self, deck, N, S, E, W, C1, C2, C3, C4):
        self.deck = deck
        self.N = N
        self.S = S
        self.E = E
        self.W = W
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.C4 = C4
        # Currently only represeting the top and bottom card for fields

        """self.Ntop = None
        self.Stop = None
        self.Etop = None
        self.Wtop = None

        self.Nbot = None
        self.Sbot = None
        self.Ebot = None
        self.Wbot = None"""
    def initfields(self):
        self.N.top = self.deck.pop()
        self.N.bot = self.N.top

        self.S.top = self.deck.pop()
        self.S.bot = self.S.top

        self.E.top = self.deck.pop()
        self.E.bot = self.E.top

        self.W.top = self.deck.pop()
        self.W.bot = self.W.top


class Game:
    # A game has a board, players p1-p4, and numplayers
    # p1 and p2 are required, with option p3 and p4
    def __init__(self, board, p1, p2, p3=0, p4=0):
        self.board = board
        self.p1 = p1
        self.p2 = p2
        self.numplayers = 2
        self.p3 = p3
        if p3 != 0:
            self.numplayers = 3
        if p4 != 0:
            self.numplayers = 4
        self.notdone = False



def initdeck(d):
    # makes each card in a deck in unshuffled order
    for i in range(0, 13):
        d.append(Card(i, 'h', 'red'))
    for i in range(0, 13):
        d.append(Card(i, 'd', 'red'))
    for i in range(0, 13):
        d.append(Card(i, 'c', 'black'))
    for i in range(0, 13):
        d.append(Card(i, 's', 'black'))
    return 52


def shuffle(d):
    random.shuffle(d)

def initboard(deck):
    N = Field()
    S = Field()
    E = Field()
    W = Field()
    C1 = Field()
    C2 = Field()
    C3 = Field()
    C4 = Field()
    board = Board(deck, N, S, E, W, C1, C2, C3, C4)
    return board

def kingscorner():
    # Start a new game by first getting the players
    numplayers = int(input("How many players? (2-4): "))
    # could error check, currently <2 gives 2 players and >4 gives 4 players
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    pname = input("Name of player 1?: ")
    p1 = Player(1, pname)
    pname2 = input("Name of player 2?: ")
    p2 = Player(2, pname2)
    if numplayers > 2:
        pname3 = input("Name of player 3?: ")
        p3 = Player(3, pname3)
    if numplayers > 3:
        pname4 = input("Name of player 4?: ")
        p4 = Player(4, pname4)

    deck = []
    count = initdeck(deck)
    shuffle(deck)
    # uncomment below to print out the deck
    """for i in range(0, count):
        deck[i].__repr__()"""
    board = initboard(deck)

    game = Game(board, p1, p2, p3, p4)

    """Here we have the game ready to go without specific rules
    game.board = the playing field
    game.board.N,S,E,W,C1,C2,C3,C4 for each field
    game.board.N.top = the current card on the field you can play a card ontop of, 0 = blank
    game.board.N.bot = the bottom card of a stack for moving how stacks
    game.p1,p2,p3,p4 for players 
    """

    # draw 7 cards each
    game.p1.newhand(deck)
    game.p2.newhand(deck)
    # play 1 card in each N,S,E,W
    game.board.initfields()

    # everything is set, now loop on turns and give rules per turn
    # while game.notdone:
        # start a turn


kingscorner()

"""ultimately, we would code this using the state machine stuff. however, since this
 +first part is supposed to be quick and dirty, we'll probably do turn order
 +as a for loop over the number of players, which a while loop inside so the player
 +may play as many cards as they desire"""