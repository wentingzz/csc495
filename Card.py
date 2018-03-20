class Card:
    def __init__(self, val, suit, color):
        # card number 0-10,J,Q,K
        self.val = val
        # card suit diamond, heart, club, spade
        self.suit = suit
        # extra color field because king's corner doesn't care about suit specifically (b or r)
        self.color = color
        # used for Ace wild card institution and reshuffling
        self.truesuit = suit

        # card value is based on the number, but is not always displayed as the number
        if val == 1:
            self.valSym = 'A'
        elif val == 11:
            self.valSym = 'J'
        elif val == 12:
            self.valSym = 'Q'
        elif val == 13:
            self.valSym = 'K'
        else:
            self.valSym = str(val)

    def __repr__(self):
        if self.val != 0:
            card = self.valSym + ' of ' + self.suit + 's'
            return card
        else:
            return 'NONE'

    # more specified card string representation for game board presentation
    def getCard(self):
        card = self.valSym + ' of ' + self.suit + 's'
        return card