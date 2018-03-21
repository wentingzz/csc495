import random

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
        return card == 13

    """
        Returns 1 if the destination field is empty
    """
    def destinationFieldIsEmpty(self, board, destinationField):
        return board.boardDic[destinationField].top.val == 0

    """
        Returns 1 if the king stack move is considered valid
    """
    def isValidKingMove(self, sourceField, destinationField, board):
        return destinationFieldIsCorner(destinationField) and cardIsKing(board.boardDic[sourceField].bot.val) and destinationFieldIsEmpty(board)

    """
        Returns 1 if the card colors of the given 2 cards alternate
    """
    def cardColorsAlternate(self, card1, card2):
        return card1.color != card2.color

    """
        Returns 1 if the card on top is 1 lower in rank than the card on bottom
    """
    def cardValuesDecrementByOne(self, cardOnTop, cardOnBottom):
        return cardOnTop.val == cardOnBottom - 1

    """
        Returns 1 if the stack (not a king) move is valid
    """
    def isValidCardMove(self, sourceField, destinationField, board):
        return destinationFieldIsEmpty(board, destinationField) and cardColorsAlternate(board.boardDic[sourceField].bot, board.boardDic[
            destinationField].top) and cardValuesDecrementByOne(board.boardDic[sourceField].bot, board.boardDic[destinationField].top)

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
        moveStack(sourceField, destinationField, board)
        board.boardDic[destinationField].bot = board.boardDic[sourceField].bot

    """
        Moves the stack from the source field on top of the stack at the destination field if the move is valid
        Returns 1 if successful
        Prints an error and returns 0 if there is a failure
    """
    def move(self, sourceField, destinationField, board):
        # check if src_field is empty
        if sourceFieldIsEmpty(sourceField, board) == 0:
            return 0
        else:
            # move Ks to any corner(empty)
            if isValidKingMove(sourceField, destinationField, board):
                moveKingStack(sourceField, destinationField, board)
            elif isValidCardMove(sourceField, destinationField, board):
                moveStack(sourceField, destinationField, board)
            else:
                print(
                    '\nError: Specifed move is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0
        return 1

    def playCardOnEmptyField(self, field, card, player):
        field.top = field.bot = card
        player.hand.remove(card)

    def playCardOnField(self, field, card, player):
        field.top = card
        player.hand.remove(card)

    """
        Plays the card from the player's hand to the board at the field specified by the player
    """
    def play(self, player, index, field, name, board):
        if checkHandSize(index, player) == 0:
            return 0
        card = player.hand[index]

        if destinationFieldIsEmpty(board, field): #field is empty
            if destinationFieldIsCorner(field): #field is in the corner
                if cardIsKing(card):
                    playCardOnEmptyField(field, card, player)
                else:
                    print('\nError: Specifed play is impossible, only Kings can be played on an empty corner, hence the name of the game...\n')
                    return 0
            elif not cardIsKing(card): #not in the corner
                playCardOnEmptyField(field, card, player)
            else:
                print('\nError: Specifed play is impossible, a king can only be played in the corner, hence the name of the game...\n')
                return 0
        else: #field is not empty, check the color and number
            if cardColorsAlternate(field.top.color, card.color) and cardValuesDecrementByOne(card.val, field.top.val):
                playCardOnField(field, card, player)
            else:
                print('\nError: Specifed play is impossible, any card placed on top of another must be of opposite color and one lower in rank\n')
                return 0
        # no errors
        return 1