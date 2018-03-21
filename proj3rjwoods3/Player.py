class Player():

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


def drawFromDeck(self, deck):
    self.hand.append(deck.pop())
    self.cc += 1

def newHand(self, deck, cardNum=7):
    for i in range(0, cardNum):
        self.drawFromDeck(deck)