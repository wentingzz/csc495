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

    def play(self, index, field, name):
        if index >= self.cc:
            print("\nError: Trying to play a card out of index of the players hand\n")
            return 0
        card = self.hand[index]
        #if the field is empty
        if field.top.val == 0:
            if name == 'c1' or name == 'c2' or name == 'c3' or name == 'c4': #field is in the corner
                if card.val == 13:
                    field.top = field.bot = card
                    self.hand.remove(card)
                else:
                    print('\nError: Specifed play is impossible, only Kings can be played on an empty corner, hence the name of the game...\n')
                    return 0
            elif card.val != 13: #not in the corner
                field.top = field.bot = card
                self.hand.remove(card)
            else:
                print('\nError: Specifed play is impossible, a king can only be played in the corner, hence the name of the game...\n')
                return 0
        else: #field is not empty, check the color and number
            if field.top.color != card.color and card.val == field.top.val - 1:
                field.top = card
                self.hand.remove(card)
            else:
                print('\nError: Specifed play is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0
        # no errors
        return 1



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
        self.boardDic = {'n': self.N, 's':self.S, 'e': self.E, 'w': self.W, 'c1': self.C1, 'c2': self.C2, 'c3': self.C3, 'c4': self.C4}
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

    def move(self, src_field, des_field):

        #check if src_field is empty
        if self.boardDic[src_field].bot.val == 0:
            print('\nError: Source field is empty\n')
            return 0
        else:
            # move Ks to any corner(empty)
            if (des_field == 'c1' or des_field == 'c2' or des_field == 'c3' or des_field == 'c4') and self.boardDic[src_field].bot.val == 13 and self.boardDic[des_field].top.val == 0:
                self.boardDic[des_field].top = self.boardDic[src_field].top
                self.boardDic[des_field].bot = self.boardDic[src_field].bot
                self.boardDic[src_field].top = self.boardDic[src_field].bot = Card(0, 'empty', 'empty')
            elif self.boardDic[des_field].top != 0 and self.boardDic[src_field].bot.color != self.boardDic[des_field].top.color and self.boardDic[src_field].bot.val == self.boardDic[des_field].top.val - 1:
                self.boardDic[des_field].top = self.boardDic[src_field].top
                self.boardDic[src_field].top = self.boardDic[src_field].bot = Card(0, 'empty', 'empty')
            else:
                print('\nError: Specifed move is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0

        return 1



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
            i = i + 1
            if i < len(player.hand):
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

class kingscorner:
    def __init__(self):
        # Start a new game by first getting the players
        numplayers = 0
        while numplayers < 2 or numplayers > 4:
            numplayers = int(input("How many players? (2-4): "))
            if numplayers < 2 or numplayers > 4:
                print("Player number must be between 2 and 4")

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
        board = initboard(deck)

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
                move = 'temp'
                turnend = 0
                p.draw(deck)
                game.printBoard(p)
                while not turnend:
                    # wait for move input
                    move = input("What will you do? (h for help): ")
                    move = move.lower()

                    if move == 'end':
                        turnend = 1
                    elif move.startswith('play'):
                        try:
                            move = move.replace(' ', '').split(':')[1]
                            stack = board.boardDic[move.split(",")[1]]
                            doprint = p.play(int(move.split(",")[0]), stack, move.split(",")[1])
                            if doprint == 1:
                                game.printBoard(p)
                        except IndexError:
                            print('Invalid syntax. Type \'h\' for a list of moves')
                    elif move.startswith('move'):
                        try:
                            move = move.replace(' ', '').split(':')[1]
                            doprint = board.move(move.split(",")[0], move.split(",")[1])
                            if doprint == 1:
                                game.printBoard(p)
                        except IndexError:
                            print('Invalid syntax. Type \'h\' for a list of moves')
                    elif move.startswith('h'):
                        try:
                            print('\"end\" \t\t\t\t\t\tto end your turn;')
                            print('\"play: card_index, destination field\" \t\tto play the card in your hand to destination field. Card index is after #;')
                            print('\"move: source field, destination field\"\t\tto move cards from source field to destination field.')
                        except IndexError:
                            print('Invalid syntax. Type \'h\' for a list of moves')
                    else:
                        print('Invalid syntax. Type \'h\' for a list of moves')

                    if len(p.hand) == 0:
                        gamewin = 1
                        winner = p.name
                        break

                if gamewin:
                    break

                input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNEXT PLAYER, PRESS ENTER WHEN READY\n')

        #this means the game has ended
        print('Congrats %s, you win~' % winner)

# start = kingscorner()







