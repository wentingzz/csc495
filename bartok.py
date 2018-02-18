import random, sys

class Card:
    def __init__(self, val, suit, color):
        # card number 0-10,J,Q,K
        self.val = val
        # card suit diamond, heart, club, spade
        self.suit = suit

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

    def play(self, index, field, name):
        1

class Board:
    # A board is made of a deck and field for playing cards
    def __init__(self, deck):
        self.deck = deck
        # Currently only represeting the top and bottom card for fields

    def initfields(self):
        1

class Game:
    # A game has a board, players p1-p4, and numplayers
    # p1 and p2 are required, with option p3 and p4
    def __init__(self, board, p1, p2, p3=0, p4=0):
        self.board = board
        self.players = []
        self.p1 = p1
        self.players.append(p1)
        self.p2 = p2
        self.players.append(p2)
        self.numplayers = 2
        self.p3 = p3
        self.p4 = p4
        if p3 != 0:
            self.numplayers = 3
            self.players.append(p3)
        if p4 != 0:
            self.numplayers = 4
            self.players.append(p4)
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
            game.players[n] for players
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
        print("Player's (%s) Hand (%d Cards):" % (player.name, len(player.hand)))
        i = 0
        for c in player.hand:
            print("(#%d - %s)" % (i, c.getCard()), end='')
            print(', ', end='')
            i = i + 1
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

def bartok():
    # Start a new game by first getting the players
    numplayers = int(input("How many players? (2-4): "))
    # could error check, currently <2 gives 2 players and >4 gives 4 players
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    players = []
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
    board = Board(deck)

    game = Game(board, p1, p2, p3, p4)

    """Here we have the game ready to go without specific rules
    game.board = the playing field
    game.board.N,S,E,W,C1,C2,C3,C4 for each field
    game.board.N.top = the current card on the field you can play a card ontop of, 0 = blank
    game.board.N.bot = the bottom card of a stack for moving how stacks
    game.players[n] for players 
    """

    # draw 7 cards each
    for p in game.players:
        p.newhand(deck)

    # play 1 card in each N,S,E,W
    game.board.initfields()


    gamewin = 0
    winner = ''
    # everything is set, now loop on turns and give rules per turn
    while not gamewin:

        #go in turn order
        for p in game.players:
            game.printBoard(p)
            move = 'temp'
            turnend = 0
            while not turnend:
                # wait for move input
                """
                not case sensitive
                    
                MOVES:
                play (card in hand) (field) -> plays the card from your hand onto the field, if possible
                    EX: play 2 of hearts E
                            IF WE HAVE TIME, do some shorthand notation
                move (field1) (field2) -> moves cards in field 1 onto field 2
                    EX: move E C1
                draw -> draws one card and ends your turn
                """
                move = input("What will you do? (h for help): ")
                move = move.lower()

                if move == 'draw':
                    p.draw(deck)
                    turnend = 1
                elif move.startswith('play'):
                    move = move.replace(' ', '').split(':')[1]
                    stack = board.boardDic[move.split(",")[1]]
                    p.play(int(move.split(",")[0]), stack, move.split(",")[1])
                    game.printBoard(p)
                    turnend = 1
                    #here we will put parsing for parameters, then call a function for playing from hand
                elif move.startswith('h'):
                    print('\"draw\" \t\t\t\t\t\tto draw a card from the desk and end your turn;')
                    print('\"play: card_index, destination field\" \t\tto play the card in your hand to destination field. Card index is in ();')
                else:
                    print('Invalid syntax')

                if len(p.hand) == 0:
                    gamewin = 1
                    winner = p.name
                    break

            if gamewin:
                break

    #this means the game has ended
    print('Congrats %s, you win~' % winner)

bartok()








