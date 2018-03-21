class BartokBoard(Board):

    """
        The only field shared by the two games is a deck
    """
    def __init__(self, deck, players, numberPlayers):
        self.deck = deck
        self.top = deck.pop()
        self.discard = []
        self.players = players
        self.numberPlayers = numberPlayers

    """
        Initializes empty field placeholders
    """
    def initfields(self):
        pass