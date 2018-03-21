import random, sys, select

class Board:
    # A board is made of a deck and field for playing cards, as well as a discard
    def __init__(self, deck):
        self.deck = deck
        self.top = deck.pop()
        self.discard = []

    def initfields(self):
        1

    def reshuffle(self):
        # shuffle the cards back into the deck, and empty discard pile
        self.deck = self.discard
        self.discard = []
        # reset all the values of the wild card aces
        for c in self.deck:
            if c.val == 1:
                c.suit == c.truesuit

        return self.deck

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

class bartok:
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
                if len(deck) <= 0:
                    deck = game.board.reshuffle()
                    print('\nReshuffling all cards under top card in field of play back into deck...\n')

                game.printBoard(p)
                move = 'temp'
                turnend = 0
                while not turnend:
                    # wait for move input
                    print ("******* You have 30 seconds to answer the following question *******")
                    print ("What will you do? (h for help): ")
                    i, o, e = select.select([sys.stdin], [], [], 30)
                    if (i):
                        move = sys.stdin.readline().strip()
                        move = move.lower()
                    else:
                        move = 'draw'

                    if move == 'draw':
                        p.draw(deck)
                        count = count - 1
                        turnend = 1
                    elif move.startswith('play'):
                        try:
                            turnend = p.play(board, int(move.split(" ")[1]))
                        except (IndexError, ValueError):
                                print('Invalid syntax. Type \'h\' for a list of moves')
                    elif move.startswith('h'):
                        try:
                            print('\"draw\"\t\t\tto draw a card from the desk and end your turn;')
                            print('\"play card_index\"\tto play the card in your hand to destination field. Card index is after #;')
                        except (IndexError, ValueError):
                            print('Invalid syntax. Type \'h\' for a list of moves')
                    else:
                        print('Invalid syntax. Type \'h\' for a list of moves')

                    if len(p.hand) == 0:
                        gamewin = 1
                        winner = p.name
                        break

                    gamewin = p.rank4()
                    if gamewin == 1:
                        winner = p.name
                        print('Player %s has all 4 cards of the same rank, so he wins!' % winner)
                        break

                if gamewin:
                    break

                input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNEXT PLAYER, PRESS ENTER WHEN READY\n')


        #this means the game has ended
        print('Congrats %s, you win~' % winner)

# start = bartok
