from collections import namedtuple

card = namedtuple("card", ["rank", "suit"])

'''


def _str_card(card):
    return f'{card.rank} of {card.suit}s'


card.__str__ = _str_card


def is_ace(card):
    return card.rank == "Ace"


card.is_ace = is_ace
'''


def is_ten(card):
    return card.rank in ["Ten", "Jack", "Queen", "King"]

# Sum draft


def sumHand(hand):
    total = 0
    for card in hand:
        total += value(card)
    if 'ace' in hand and total < 12:
        total += 10
    return total


class Deck:
    ranks = ["Ace" + str([str(x) for x in range(2, 11)]) +
             "Jack Queen King".split()]
    suits = ["Club", "Heart", "Spade", "Diamond"]
    values = list(range(1, 11)) + [10, 10, 10]
    valueDict = dict(zip(ranks, values))

    def __init__(self):
        self._cards = [card("rank", "suit")
                       for suit in self.suits for rank in self.ranks]
        self._marker = len(self._cards) * .25

    def deal_cards(self, n=1):
        return [self._cards.pop() for x in range(n)]

    def merge_cards(self, other):
        self._cards = self._cards + other._cards
        # Update marker

    def shuffle_cards(self):


my_deck = Deck

print(my_deck.ranks)
