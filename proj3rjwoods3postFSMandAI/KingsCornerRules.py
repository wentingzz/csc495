import random
from Rules import Rules
from Card import Card

class KingsCornerRules(Rules):

    """
        Prints the ASCII representation of the current board layout
        This includes the 4 corners, the NEWS, and middle deck
    """
    def printBoardSpace(self, board):
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     | Top: %16s     | Top: %16s     |' % (board.C1.top, board.N.top, board.C2.top,))
        print('|                           |                           |                           |')
        print('|            ****           |            ***            |            ****           |')
        print('|            *C1*           |            *N*            |            *C2*           |')
        print('|            ****           |            ***            |            ****           |')
        print('|                           |                           |                           |')
        print('| Bottom: %13s     | Bottom: %13s     | Bottom: %13s     |' % (board.C1.bot, board.N.bot, board.C2.bot,))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     |                           | Top: %16s     |' % (board.W.top, board.E.top, ))
        print('|                           |                           |                           |')
        print('|            ***            |                           |            ***            |')
        print('|            *W*            |           DECK            |            *E*            |')
        print('|            ***            |          %2d CARDS         |            ***            |' % len(board.deck))
        print('|                           |                           |                           |')
        print('| Bottom: %13s     |                           | Bottom: %13s     |' % (board.W.bot, board.E.bot))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print('|                           |                           |                           |')
        print('| Top: %16s     | Top: %16s     | Top: %16s     |' % (board.C3.top, board.S.top, board.C4.top))
        print('|                           |                           |                           |')
        print('|            ****           |            ***            |            ****           |')
        print('|            *C3*           |            *S*            |            *C4*           |')
        print('|            ****           |            ***            |            ****           |')
        print('|                           |                           |                           |')
        print('| Bottom: %13s     | Bottom: %13s     | Bottom: %13s     |' % (board.C3.bot, board.S.bot, board.C4.bot))
        print('|                           |                           |                           |')
        print('*---------------------------*---------------------------*---------------------------*')
        print()

    """
        Returns 1 if the source field is empty
    """
    def sourceFieldIsEmpty(self, sourceField, board):
        if board.boardDic[sourceField].bot.val == 0:
            print('\nError: Source field is empty\n')
            return 0
        return 1


    """
        Returns 1 if the destination field is a corner field
    """
    def destinationFieldIsCorner(self, destinationField):
        return destinationField == 'c1' or destinationField == 'c2' or destinationField == 'c3' or destinationField == 'c4'

    """
        Returns 1 if the given card is a king
    """
    def cardIsKing(self, card):
        return card.val == 13

    """
        Returns 1 if the destination field is empty
    """
    def destinationFieldIsEmpty(self, board, destinationField):
        return board.boardDic[destinationField].top.val == 0

    """
        Returns 1 if the king stack move is considered valid
    """
    def isValidKingMove(self, sourceField, destinationField, board):
        return self.destinationFieldIsCorner(destinationField) and self.cardIsKing(board.boardDic[sourceField].bot) and self.destinationFieldIsEmpty(board, destinationField)

    """
        Returns 1 if the card colors of the given 2 cards alternate
    """
    def cardColorsAlternate(self, card1, card2):
        return card1.color != card2.color

    """
        Returns 1 if the card on top is 1 lower in rank than the card on bottom
    """
    def cardValuesDecrementByOne(self, cardOnTop, cardOnBottom):
        return cardOnTop.val == cardOnBottom.val - 1

    """
        Returns 1 if the stack (not a king) move is valid
    """
    def isValidCardMove(self, sourceField, destinationField, board):
        return self.destinationFieldIsEmpty(board, destinationField) or (self.cardColorsAlternate(board.boardDic[sourceField].bot, board.boardDic[
            destinationField].top) and self.cardValuesDecrementByOne(board.boardDic[sourceField].bot, board.boardDic[destinationField].top))

    """
        Moves the stack from the source field on top of the stack at the destination field
    """
    def moveStack(self, sourceField, destinationField, board):
        board.boardDic[destinationField].top = board.boardDic[sourceField].top
        board.boardDic[sourceField].top = board.boardDic[sourceField].bot = Card(0, 'empty', 'empty')

    """
        Moves the (king) stack from the source field on top of the stack at the destination field
    """
    def moveKingStack(self, sourceField, destinationField, board):
        board.boardDic[destinationField].top = board.boardDic[sourceField].top
        board.boardDic[destinationField].bot = board.boardDic[sourceField].bot
        board.boardDic[sourceField].top = board.boardDic[sourceField].bot = Card(0, 'empty', 'empty')

    """
        Moves the stack from the source field on top of the stack at the destination field if the move is valid
        Returns 1 if successful
        Prints an error and returns 0 if there is a failure
    """
    def move(self, sourceField, destinationField, board):
        # check if src_field is empty
        if self.sourceFieldIsEmpty(sourceField, board) == 0:
            return 0
        else:
            # move Ks to any corner(empty)
            if self.isValidKingMove(sourceField, destinationField, board):
                self.moveKingStack(sourceField, destinationField, board)
            elif self.isValidCardMove(sourceField, destinationField, board):
                self.moveStack(sourceField, destinationField, board)
            else:
                print(
                    '\nError: Specifed move is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0
        return 1

    """
        Plays the given card on the given empty field by setting the top and bottom card
        to the new card and removing it from the player's hand
    """
    def playCardOnEmptyField(self, field, card, player):
        field.top = field.bot = card
        player.hand.remove(card)

    """
        Plays the given card on the top of the given field by changing the top card to the
        card and removing it from the player's hand.
    """
    def playCardOnField(self, field, card, player):
        field.top = card
        player.hand.remove(card)

    """
        Plays the card from the player's hand to the board at the field specified by the player
    """
    def play(self, player, index, field, fieldName, board):
        if self.checkHandSize(index, player) == 0:
            return 0
        card = player.hand[index]

        if self.destinationFieldIsEmpty(board, fieldName): #field is empty
            if self.destinationFieldIsCorner(fieldName): #field is in the corner
                if self.cardIsKing(card):
                    self.playCardOnEmptyField(field, card, player)
                else:
                    print('\nError: Specifed play is impossible, only Kings can be played on an empty corner, hence the name of the game...\n')
                    return 0
            elif not self.cardIsKing(card): #not in the corner
                self.playCardOnEmptyField(field, card, player)
            else:
                print('\nError: Specifed play is impossible, a king can only be played in the corner, hence the name of the game...\n')
                return 0
        else: #field is not empty, check the color and number
            if self.cardColorsAlternate(field.top, card) and self.cardValuesDecrementByOne(card, field.top):
                self.playCardOnField(field, card, player)
            else:
                print('\nError: Specifed play is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0
        # no errors
        return 1

    """
        Ends the player's turn
    """
    def endTurn(self, player, board, move):
        return 1

    """
        Attempt to play a card from the hand. If any errors or issues arise, they are
        caught and expressed to the player.
    """
    def tryToPlay(self, player, board, move):
        try:
            move = move.replace(' ', '').split(':')[1]
            stack = board.boardDic[move.split(",")[1]]
            doprint = self.play(player, int(move.split(",")[0]), stack, move.split(",")[1], board)
            if doprint == 1:
                self.printBoard(board, player)
        except (IndexError, KeyError):
            print('Invalid syntax. Type \'h\' for a list of moves')

    """
        Attempt to move a stack from one field to another. If any errors or issues arise, they are
        caught and expressed to the player.
    """
    def tryToMove(self, player, board, move):
        try:
            move = move.replace(' ', '').split(':')[1]
            doprint = self.move(move.split(",")[0], move.split(",")[1], board)
            if doprint == 1:
                self.printBoard(board, player)
        except (IndexError, KeyError):
            print('Invalid syntax. Type \'h\' for a list of moves')

    """
        Prints the list of commands available to the player
    """
    def printHelp(self, player, board, move):
        try:
            print('\"end\" \t\t\t\t\t\tto end your turn;')
            print('\"play: card_index, destination field\" \t\tto play the card in your hand to destination field. Card index is after #;')
            print('\"move: source field, destination field\"\t\tto move cards from source field to destination field.')
        except IndexError:
            print('Invalid syntax. Type \'h\' for a list of moves')

    """
        Determines if the given player has won due to not having any cards in their hand
    """
    def determineIfPlayerHasWon(self, player):
        return self.isWinnerByNoHand(player)