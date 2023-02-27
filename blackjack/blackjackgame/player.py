# Simon Lariz
# CPSC 386-02
# 2023-02-26
# simonlariz@csu.fullerton.edu
# @SimonLariz
#
# Lab 00-02
#
# This is the player module for the blackjack game.
#

"""This module contains the Player class and related functions."""


class Player:
    """A class representing a player in the blackjack game."""

    def __init__(self, name, money=10000):
        self.name = name
        self.money = money
        self.hand = []
        self.bet = 0
        self.bust = False
        self.blackjack = False
        self.hit = True

    def get_name(self):
        """Returns the name of the player."""
        return self.name

    def get_money(self):
        """Returns the amount of money the player has."""
        return self.money

    def get_bet(self):
        """Returns the amount of money the player has bet."""
        return self.bet

    def get_hand(self):
        """Returns the player's hand."""
        return self.hand

    def set_money(self, money):
        """Sets the amount of money the player has."""
        self.money = money

    def set_bet(self, bet):
        """Sets the amount of money the player has bet."""
        self.bet = bet

    def set_hand(self, hand):
        """Sets the player's hand."""
        self.hand = hand

    def add_card(self, card):
        """Adds a card to the player's hand."""
        self.hand.append(card)

    def get_hit(self):
        """Returns whether the player wants to hit or not."""
        return self.hit

    def set_hit(self, hit):
        """Sets whether the player wants to hit or not."""
        self.hit = hit

    def get_bust(self):
        """Returns whether the player has busted or not."""
        return self.bust

    def set_bust(self, bust):
        """Sets whether the player has busted or not."""
        self.bust = bust

    def reset_player(self):
        """Resets the player's attributes to their default values."""
        self.hand = []
        self.bet = 0
        self.bust = False
        self.blackjack = False
        self.hit = True
