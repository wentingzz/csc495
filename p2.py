import random, sys


class Card:
    def __init__(self, val, suit, color):
        self.val = val
        self.suit = suit
        self.color = color

    def __repr__(self):
        print("Card value: " + str(self.val))
        print("Card suit: " + self.suit)
        print("Card color: " + self.color)
        print()
class Player:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.hand = []
        self.cc = 0

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
        return self.hand.pop([index])


class Field:
    def __init__(self):




class Board:
    def __init__(self, N, S, E, W, C1, C2, C3, C4):
        """self.N = []
        self.S = []
        self.E = []
        self.W = []
        self.C1 = []
        self.C2 = []
        self.C3 = []
        self.C4 = []

        self.Ntop = None
        self.Stop = None
        self.Etop = None
        self.Wtop = None

        self.Nbot = None
        self.Sbot = None
        self.Ebot = None
        self.Wbot = None"""


def initdeck(d, c):
    for i in range(0, 13):
        d.append(Card(i, 'h', 'red'))
        c += 1
    for i in range(0, 13):
        d.append(Card(i, 'd', 'red'))
        c += 1
    for i in range(0, 13):
        d.append(Card(i, 'c', 'black'))
        c += 1
    for i in range(0, 13):
        d.append(Card(i, 's', 'black'))
        c += 1
    return c


def shuffle(d):
    random.shuffle(d)






count = 0
deck = []
count = initdeck(deck, count)

# print(count)
shuffle(deck)


for i in range(0, count):
    deck[i].__repr__()



"""ultimately, we would code this using the state machine stuff. however, since this
first part is supposed to be quick and dirty, we'll probably do turn order
as a for loop over the number of players, which a while loop inside so the player
may play as many cards as they desire"""