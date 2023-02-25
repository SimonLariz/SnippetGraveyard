import random
from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


def _str_card(card):
    return f"{card.rank} of {card.suit}s"


def is_ace(card):
    return card.rank == "Ace"


def is_face_card(card):
    return card.rank in ["Jack", "Queen", "King"]


def get_value(card):
    if is_ace(card):
        return 1
    elif is_face_card(card):
        return 10
    else:
        return int(card.rank)


def sum_hand(hand):
    total = 0
    for card in hand:
        total += get_value(card)
        if is_ace(card) and total <= 11:
            total += 10
    return total


def format_card_text(hand, hidden=False):
    rank_name = ["Ace", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "Jack", "Queen", "King"]
    rank_symbol = ["A", "2", "3", "4", "5",
                   "6", "7", "8", "9", "10", "J", "Q", "K"]
    rank = rank_symbol[rank_name.index(card.rank)]
    suit_name = ["spade", "heart", "diamond", "club"]
    suit_symbol = ["♠", "♥", "♦", "♣"]
    hidden_symbol = "?"
    suit = suit_symbol[suit_name.index(card.suit)]
    if hidden:
        rank = hidden_symbol
        suit = hidden_symbol

    return (display_card)


Card.__str__ = _str_card


class FrenchDeck:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["spade", "heart", "diamond", "club"]

    def __init__(self, num_decks):
        self._cards = []
        for x in range(num_decks):
            self._cards += [Card(rank, suit)
                            for suit in self.suits for rank in self.ranks]
        self._marker = int(len(self._cards) * .75 + random.randint(0, 10))

    def __len__(self):
        return len(self._cards)

    def deal(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    def cut(self):
        self._cards = self._cards[self._marker:] + self._cards[:self._marker]


'''

print("my_deck = FrenchDeck()")
my_deck = FrenchDeck(1)

my_deck.shuffle()
my_deck.cut()

for card in my_deck._cards:
    print(str(card))

player_hands = [[], []]

# deal 2 cards one at a time to each player
for i in range(2):
    for hand in player_hands:
        hand.append(my_deck.deal())

print("player_hands = ", player_hands)

print("\n\n")

'''
