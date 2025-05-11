class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

# Create a new Card object
card = Card("Hearts", "Ace")

# Print the Card
print(card)  # Output: Ace of Hearts

# Compare two Card objects
card2 = Card("Hearts", "Ace")
print(card == card2)  # Output: True