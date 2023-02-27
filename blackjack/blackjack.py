#! /usr/bin/env python3
# Simon Lariz
# CPSC 386-02
# 2023-02-22
# simonlariz@csu.fullerton.edu
# @SimonLariz
#
# Lab 00-02
#
# This program is a simple blackjack game.
#

"""blackjackgame package, contains all blackjack game modules."""
from blackjackgame import game


def main():
    """Calls main game loop from blackjackgame.game module."""
    return game.main_game_loop()


if __name__ == "__main__":
    main()
