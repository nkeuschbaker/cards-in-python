class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value
