import random, sys

class Card:
    def __init__(self, val, suit, color):
        # card number 0-10,J,Q,K
        self.val = val
        # card suit diamond, heart, club, spade
        self.suit = suit
        # extra color field because king's corner doesn't care about suit specifically (b or r)
        self.color = color



        # card value is based on the number, but is not always displayed as the number
        if val == 1:
            self.valSym = 'A'
        elif val == 11:
            self.valSym = 'J'
        elif val == 12:
            self.valSym = 'Q'
        elif val == 13:
            self.valSym = 'K'
        else:
            self.valSym = str(val)

    def __repr__(self):
        if self.val != 0:
            card = self.valSym + ' of ' + self.suit + 's'
            return card
        else:
            return 'NONE'

    # more specified card string representation for game board presentation
    def getCard(self):

        card = self.valSym + ' of ' + self.suit + 's'
        return card

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

    def playOnto(self, card):
        1
        # change top card if applicable

    def moveToField(self, stack):
        1
        # move this stack to the top of another stack

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

class Game:
    # A game has a board, players p1-p4, and numplayers
    # p1 and p2 are required, with option p3 and p4
    def __init__(self, board, p1, p2, p3=0, p4=0):
        self.board = board
        self.p1 = p1
        self.p2 = p2
        self.numplayers = 2
        self.p3 = p3
        self.p4 = p4
        if p3 != 0:
            self.numplayers = 3
        if p4 != 0:
            self.numplayers = 4
        self.notdone = False

    # prints an ASCII display of the current player's view of the game board
    # this will include the playing field, the cards, show the hand to the player given, and the number of cards in
    # other player's hands
    def printBoard(self, player):

        """Here we have the game ready to go without specific rules
            game.board = the playing field
            game.board.N,S,E,W,C1,C2,C3,C4 for each field
            game.board.N.top = the current card on the field you can play a card ontop of, 0 = blank
            game.board.N.bot = the bottom card of a stack for moving how stacks
            game.p1,p2,p3,p4 for players
            """


        #print the board
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     | Top: %16s     | Top: %16s     |' % (self.board.C1.top, self.board.N.top, self.board.C2.top,))
        print('|                           |                           |                           |')
        print('|            ****           |            ***            |            ****           |')
        print('|            *C1*           |            *N*            |            *C2*           |')
        print('|            ****           |            ***            |            ****           |')
        print('|                           |                           |                           |')
        print('| Bottom: %13s     | Bottom: %13s     | Bottom: %13s     |' % (self.board.C1.bot, self.board.N.bot, self.board.C2.bot,))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     |                           | Top: %16s     |' % ( self.board.W.top, self.board.E.top, ))
        print('|                           |                           |                           |')
        print('|            ***            |                           |            ***            |')
        print('|            *W*            |           DECK            |            *E*            |')
        print('|            ***            |          %2d CARDS         |            ***            |' % len(self.board.deck))
        print('|                           |                           |                           |')
        print('| Bottom: %13s     |                           | Bottom: %13s     |' % (self.board.W.bot, self.board.E.bot))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     | Top: %16s     | Top: %16s     |' % (self.board.C3.top,self.board.S.top,  self.board.C4.top))
        print('|                           |                           |                           |')
        print('|            ****           |            ***            |            ****           |')
        print('|            *C3*           |            *S*            |            *C4*           |')
        print('|            ****           |            ***            |            ****           |')
        print('|                           |                           |                           |')
        print('| Bottom: %13s     | Bottom: %13s     | Bottom: %13s     |' % (self.board.C3.bot,  self.board.S.bot, self.board.C4.bot))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print()

        #player's hand
        print("Player's Hand (%d Cards):" % (len(player.hand)))
        for c in player.hand:
            print(c.getCard(), end='')
            print(', ', end='')
        print('')
        print('')

        #player hand numbers
        print('Number of Cards in Each Player\'s Hand:')
        print(self.p1.name + ': ' + str(len(self.p1.hand)))
        print(self.p2.name + ': ' + str(len(self.p2.hand)))
        if self.numplayers >= 3:
            print(self.p3.name + ': ' + str(len(self.p3.hand)))
        if self.numplayers >= 4:
            print(self.p4.name + ': ' + str(len(self.p4.hand)))
        print('')





"""Here we have the game ready to go without specific rules
    game.board = the playing field
    game.board.N,S,E,W,C1,C2,C3,C4 for each field
    game.board.N.top = the current card on the field you can play a card ontop of, 0 = blank
    game.board.N.bot = the bottom card of a stack for moving how stacks
    game.p1,p2,p3,p4 for players 
    """

def initdeck(d):
    # makes each card in a deck in unshuffled order
    for i in range(1, 14):
        d.append(Card(i, 'Heart', 'Red'))
    for i in range(1, 14):
        d.append(Card(i, 'Diamond', 'Red'))
    for i in range(1, 14):
        d.append(Card(i, 'Club', 'Black'))
    for i in range(1, 14):
        d.append(Card(i, 'Spade', 'Black'))
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
    if numplayers >= 3:
        game.p3.newhand(deck)
    if numplayers >= 4:
        game.p4.newhand(deck)

    # play 1 card in each N,S,E,W
    game.board.initfields()

    game.printBoard(p1)





    # everything is set, now loop on turns and give rules per turn
    #while 1:
    #    for turn in range(numplayers):
   #         turnend = false
    #        while not turnend:
     #           1
     #           # wait for move input



kingscorner()








