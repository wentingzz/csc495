import sys, select

class State():
  def __init__(self, name, ruleName):
    self.name, self.ruleName = name, ruleName

  def execute(self, currentPlayer, board, move):
    return self.ruleName(currentPlayer, board, move)

  def check(self, rule, player):
    return rule.determineIfPlayerHasWon(player)

class BartokStartState(State):
  def execute(self, rule, currentPlayer, board):
    rule.reshuffleBartok(board)
    rule.printBoard(board, currentPlayer)


class KingStartState(State):
  def execute(self, rule, currentPlayer, board):
    currentPlayer.drawFromDeck(board.deck)
    rule.printBoard(board, currentPlayer)



class Machine:
  def __init__(self, name, rules, players, numplayers, deck, board):
    self.name, self.rules, self.players, self.numplayers, self.deck, self.board = name, rules, players, numplayers, deck, board
    # self.states = {"draw": State("Draw", "drawCardAndEndTurn"), "play" : State("Play","tryToPlay"), "h" : State("Help","printHelp")}
    self.states = {}
    self.currentState = None

  def Bstart(self):
    self.states.update({"newTurn": BartokStartState("NewTurn", [self.rules.reshuffleBartok, self.rules.printBoard])})

  def Kstart(self):
    self.states.update({"newTurn": BartokStartState("NewTurn", [self.rules.reshuffleBartok, self.rules.printBoard])})

  def addState(self, input, stateName, rule):
    self.states.update({input : State(stateName, rule)})


  def getMoveFromPlayer(self):
    move = input("What will you do? (h for help): ")
    move = move.lower()

    return move
  def run(self): ### AI doesn't know what to do if the card is A
    winner = None
    while winner == None:
      # go in turn order
      for p in range(self.numplayers):
        #begining of each turn
        currentPlayer = self.players[p + 1]
        self.currentState = self.states["newTurn"]
        self.currentState.execute(self.rules, currentPlayer, self.board)

        turnend = 0
        while not turnend:
          #a player's turn
          move = currentPlayer.nextstep(self.board)
          try:
            self.currentState = self.states[move[:4]]
            turnend = self.currentState.execute(currentPlayer, self.board, move)
            winner = self.currentState.check(self.rules, currentPlayer)
            if winner != None:
              break
          except:
            print('Invalid syntax. Type \'h\' for a list of moves')
        if winner != None:
          break
        input(
          '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNEXT PLAYER, PRESS ENTER WHEN READY\n')
    # this means the game has ended
    print('Congrats %s, you win~' % winner)
    return "" #winner's name
