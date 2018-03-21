import random

class BartokRules(Rules):

    """
        Prints the ASCII representation of the current board layout
    """
    def printBoardSpace(self, board):
        print('*---------------------------*                           *---------------------------*')
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('|           DECK            |                           |          PLAYED           |')
        print('|          %2d CARDS         |                           |       %13s       |' % (
        len(board.deck), board.top))
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('|                           |                           |                           |')
        print('*---------------------------*                           *---------------------------*')



    """
        Returns 1 if the given card is an Ace that can be used as a wild card in Bartok
    """
    def isWildAce(self, card):
        return card.val == 1

    """
        Prompts the user for the suit to change the ace to before playing it on the pile
    """
    def playWildAce(self, card, player, board):
        # prompt user for wild card suit choosing
        tempsuit = card.suit
        suitd = input(
            'Please enter the first letter of the suit you wish for this Ace to represent (s, h, d, or c): ').lower()
        if suitd == 's':
            card = Card(1, 'Spade', 'Blank')
        elif suitd == 'd':
            card = Card(1, 'Diamond', 'Red')
        elif suitd == 'h':
            card = Card(1, 'Heart', 'Red')
        elif suitd == 'c':
            card = Card(1, 'Club', 'Black')
        else:
            print('Invalid option, please try playing the card again')
            return 0

        card.truesuit = tempsuit
        board.discard.append(board.top)
        board.top = card
        player.hand.remove(player.hand[index])
        player.cc = player.cc - 1
        return 1

    """
        Returns 1 if the given card matches the top of the pile, in either suit or rank
    """
    def topCardMatch(self, card, board):
        return board.top.suit == card.suit or board.top.val == card.val

    """
        Plays a card on the top of the pile
    """
    def playNormalCard(self, card, player, board):
        board.discard.append(board.top)
        board.top = card
        player.hand.remove(player.hand[index])
        player.cc = player.cc - 1

    """
        Plays the card at the given index of the player's hand to the top of the pile, if valid
    """
    def play(self, player, index, field, name, board):
        if checkHandSize(index, player) == 0:
            return 0
        else:
            card = player.hand[index]
            if isWildAce(card):
                return playWildAce(card, player, board)
            elif topCardMatch(card, board):
                return playNormalCard(card, player, board)
            print('Card played must be of the same rank or suit as face up on playing stack')
            return 0