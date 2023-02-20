# init.py
__all__ = ["deck", "player", "game"]

# blackjack.py

from blackjackgame import *

if __name__ == "__main__":
    game.BlackjackGame().run()

# deck
# player


class Player:
    def __init__(self, name, bankroll=1000):
        self._name = name
        self._bankroll = bankroll
        self.hands = []

    @property
    def name(self):
        return self._name

    @property
    def bankroll(self):
        return self._bankroll
