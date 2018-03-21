import random
from Card import Card

class Rules():

    """
        Moves a stack from the source field to the destination field if the move is valid
    """
    def move(self, sourceField, destinationField):
        pass

    """
        Plays a card from the player's hand to the board
        Different for each game
    """
    def play(self, player, index, field, name, board):
        pass

    """
        Checks that the index given is not out of range of the player's hand
        Used to make sure the player isn't trying to play a card not in their hand
    """
    def checkHandSize(self, index, player):
        if index >= player.cc:
            print("Error: Trying to play a card out of index of the players hand")
            return 0
        return 1

    """
        Prints the ASCII representation of the current board layout
        Different for each game
    """
    def printBoardSpace(self, board):
        pass

    """
        Prints the number of cards in each player's hands
    """
    def printPlayerHandNumbers(self, numberPlayers, players):
        print('Number of Cards in Each Player\'s Hand:')
        for p in range(numberPlayers):
            print(players[p].name + ': ' + str(len(players[p].hand)))
        print('')

    """
        Prints the cards in the given player's hands
    """
    def printPlayerHand(self, player):
        print("Player's (%s) Hand (%d Cards):" % (player.name, len(player.hand)))
        i = 0
        for c in player.hand:
            print("(#%d - %s)" % (i, c.getCard()), end='')
            i = i + 1
            if i < len(player.hand):
                print(', ', end='')
        print('')
        print('')

    """
        Prints the instance of a player's turn; including the board, player hand counts, and the current player's hands
    """
    def printBoard(self, board, player):
        printBoardSpace(board)
        printPlayerHand(player)
        printPlayerHandNumbers(board.numberPlayers, board.players)

    """
        Creates a deck by creating all 52 cards then shuffling. Returns the deck.
    """
    def createDeck(self, deck):
        for i in range(1, 14):
            deck.append(Card(i, 'Heart', 'Red'))
        for i in range(1, 14):
            deck.append(Card(i, 'Diamond', 'Red'))
        for i in range(1, 14):
            deck.append(Card(i, 'Club', 'Black'))
        for i in range(1, 14):
            deck.append(Card(i, 'Spade', 'Black'))
        shuffle(deck)
        return len(deck)

    """
        Shuffles the given deck
    """
    def shuffle(self, deck):
        random.shuffle(deck)

    """
        If the given player has all 4 copies of a certain card rank, returns 1 so that they can be declared the winner
    """
    def fourOfSameRank(self, player):
        ranks = {"A": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0,
                 "K": 0}
        for card in player.hand:
            ranks[card.valSym] = ranks[card.valSym] + 1
        for i in ranks:
            if ranks[i] == 4:
                return 1
        return 0

    """
        Resets the suit of all aces in the deck after being changed by wild card rules
    """
    def resetAces(self, deck):
        for card in deck:
            if card.val == 1:
                card.suit == card.truesuit

    """
        Shuffles the cards back into the deck, and empties the discard pile
    """
    def reshuffle(self, board):
        board.deck = board.discard
        board.discard = []
        resetAces(board.deck)
        return self.deck