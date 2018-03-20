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


def newhand(self, d, repeat=7):
    for i in range(0, repeat):
        self.draw(d)