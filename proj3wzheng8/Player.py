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
        if len(deck) > 0:
            self.hand.append(deck.pop())
            self.cc += 1

    def newHand(self, deck, cardNum=7):
        for i in range(0, cardNum):
            self.drawFromDeck(deck)

    def nextstep(self, borad):
        move = input("What will you do? (h for help): ")
        return move.lower()

class BartokAIPlayer(Player):

    def nextstep(self, board):
        print ("What will you do? (h for help): ")
        index = self.validIndexToPlay(board)
        if index == -1:
            action = 'draw'
        else:
            action = 'play ' + str(index)
        print(action)
        return action

    def validIndexToPlay(self, board):
        for i in range(len(self.hand)):
            if self.hand[i].sameSuit(board.top) or self.hand[i].sameNumber(board.top):
                return i
        return -1

class KingsAIPlayer(Player):
    def nextstep(self, board):
        print ("What will you do? (h for help): ")
        action = self.validPlay(board)
        if action[0] == -1:                 #cannot play any card on hand
            action = self.validMove(board)  #try to move card on board
            if action[0] == -1:             #no valid move
                action = 'end'              #end the turn
            else:                           #valid move
                action = 'move: ' + action[0] + ', ' + action[1]
        else:                               #valid play
            action = 'play: ' + str(action[0]) + ', ' + action[1]
        print(action)
        return action

    def validPlay(self, board):
        #play K to the corner (get all the empty fields -> play K)
        fieldsName = ['n', 's', 'e', 'w']
        for i in range(len(self.hand)):
            if self.hand[i].val == 13:
                if board.boardDic['c1'].top.val == 0:
                    return [i, 'c1']
                elif board.boardDic['c2'].top.val == 0:
                    return [i, 'c2']
                elif board.boardDic['c3'].top.val == 0:
                    return [i, 'c3']
                elif board.boardDic['c4'].top.val == 0:
                    return [i, 'c4']

        # play the card to the empty field(not the corner)
        for name in fieldsName:
            if board.boardDic[name].top.val == 0:
                return [0, name]

        # play card to a non-empty field
        for key, field in board.boardDic.items():
            if field.top != 0:                          #the field is not empty
                for i in range(len(self.hand)):         #check cards on hand
                    if self.hand[i].diffColor(field.top) and self.hand[i].val == field.top.val - 1:
                        return [i, key]

        #no card can be played
        return [-1, ""]


    def validMove(self, board):
        #move K to the corner
        fieldsName = ['n','s','e','w']
        allFieldsName = ['n', 's', 'e', 'w', 'c1', 'c2', 'c3', 'c4']
        cornerName = ['c1', 'c2', 'c3', 'c4']
        for name in fieldsName:
            if board.boardDic[name].bot.val == 13:
                for dest in cornerName:
                    if board.boardDic[dest].top.val == 0:
                        return [name, dest]

        #no K on the board to move: try to move fields
        for source in fieldsName:
            for destination in allFieldsName:
                sCard = board.boardDic[source].bot
                dCard = board.boardDic[destination].top
                if sCard.diffColor(dCard) and sCard.val == dCard.val - 1 :
                    return [source, destination]
        return [-1, ""]