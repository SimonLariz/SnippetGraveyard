
"""This module contains the Card class and related functions."""

import random
from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


def _str_card(card):
    """Returns a string representation of a card."""
    return f"{card.rank} of {card.suit}s"


def is_ace(card):
    """Returns True if card is an Ace, False otherwise."""
    return card.rank == "Ace"


def is_face_card(card):
    """Returns True if card is a face card, False otherwise."""
    return card.rank in ["Jack", "Queen", "King"]


def get_value(card):
    """Returns the value of a card."""
    if is_ace(card):
        return 1
    if is_face_card(card):
        return 10
    return int(card.rank)


def sum_hand(hand):
    """Returns the sum of a hand of cards."""
    total = 0
    for card in hand:
        total += get_value(card)
        if is_ace(card) and total <= 11:
            total += 10
    return total


def format_hand(hand, hidden=False):
    """Returns a formatted string representation of a hand of cards."""
    rank_name = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    rank_symbol = [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
    ]
    suit_name = ["spade", "heart", "diamond", "club"]
    suit_symbol = ["♠", "♥", "♦", "♣"]
    hidden_card = """
        ┌──────────┐
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        │░░░░░░░░░░│
        └──────────┘""".split(
        "\n"
    )

    str_hand_formatted = []
    if hidden:
        str_hand_formatted.append(hidden_card)
        hand = hand[1:]

    for card in hand:
        rank = rank_symbol[rank_name.index(card.rank)]
        suit = suit_symbol[suit_name.index(card.suit)]
        if card.rank == "10":
            space_char = ""
        else:
            space_char = " "

        str_card_formatted = f"""
        ┌──────────┐
        │{rank}{space_char}        │
        │          │
        │          │
        │     {suit}    │
        │          │
        │          │
        │        {space_char}{rank}│
        └──────────┘""".split(
            "\n"
        )
        str_hand_formatted.append(str_card_formatted)

    for i in zip(*str_hand_formatted):
        print("".join(i))


Card.__str__ = _str_card


class FrenchDeck:
    """A class representing a deck of cards."""

    ranks = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    suits = ["spade", "heart", "diamond", "club"]

    def __init__(self, num_decks):
        self._cards = []
        for _ in range(num_decks):
            self._cards += [
                Card(rank, suit) for suit in self.suits for rank in self.ranks
            ]
        self.marker = int(len(self._cards) * 0.75 + random.randint(0, 10))

    def __len__(self):
        """Returns the number of cards in the deck."""
        return len(self._cards)

    def deal(self):
        """Returns the top card of the deck."""
        return self._cards.pop()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self._cards)

    def cut(self):
        """Cuts the deck."""
        self._cards = self._cards[self.marker :] + self._cards[: self.marker]
