class Field():

    # A field is a playable location for cards (N is a field, a corner is a field)
    def __init__(self):
        # Using 0 as the representation of an empty field
        self.top = 0
        self.bot = 0

    def getTopCard(self):
        return self.top

    def getBottomCard(self):
        return self.bot

