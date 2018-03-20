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
    1

def move(self, src_field, des_field):
    # check if src_field is empty
    if self.boardDic[src_field].bot.val == 0:
        print('\nError: Source field is empty\n')
        return 0
    else:
        # move Ks to any corner(empty)
        if (des_field == 'c1' or des_field == 'c2' or des_field == 'c3' or des_field == 'c4') and self.boardDic[
            src_field].bot.val == 13 and self.boardDic[des_field].top.val == 0:
            self.boardDic[des_field].top = self.boardDic[src_field].top
            self.boardDic[des_field].bot = self.boardDic[src_field].bot
            self.boardDic[src_field].top = self.boardDic[src_field].bot = Card(0, 'empty', 'empty')
        elif self.boardDic[des_field].top != 0 and self.boardDic[src_field].bot.color != self.boardDic[
            des_field].top.color and self.boardDic[src_field].bot.val == self.boardDic[des_field].top.val - 1:
            self.boardDic[des_field].top = self.boardDic[src_field].top
            self.boardDic[src_field].top = self.boardDic[src_field].bot = Card(0, 'empty', 'empty')
        else:
            print(
                '\nError: Specifed move is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
            return 0

    return 1

def play(self, index, field, name):
    1

def shuffle(d):
    random.shuffle(d)

def reshuffle(self):
    # shuffle the cards back into the deck, and empty discard pile
    self.deck = self.discard
    self.discard = []
    # reset all the values of the wild card aces
    for c in self.deck:
        if c.val == 1:
            c.suit == c.truesuit
    return self.deck

def initboard(deck):
    1

# if you have 4 of the same rank, you win
def rank4(self):
    ranks = {"A": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0}
    for c in self.hand:
        ranks[c.valSym] = ranks[c.valSym] + 1
    for i in ranks:
        if ranks[i] == 4:
            return 1
    return 0

def beginGame():
    1