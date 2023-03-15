
"""This module contains the Card class and related functions."""
import os
import os.path
import pickle
from blackjackgame.cards import FrenchDeck, sum_hand, format_hand
from blackjackgame.player import Player


class Game:
    """This class contains the game logic for the blackjack game."""

    def __init__(self, num_players, num_decks):
        self.deck = FrenchDeck(num_decks)
        self.num_players = num_players
        self.players = []
        for player_num in range(num_players):
            player_name = input(
                "What is player " + str(player_num + 1) + "'s name? "
            )
            self.players.append(Player(player_name))
        self.dealer = Player("DEALER")
        self.num_players_busted = 0
        self.cards_dealt = 0
        self.cut_card_reached = False

    def deal_cards(self):
        """Deal the cards to the players and dealer."""
        marker_position = self.deck.marker
        for player in self.players:
            for _ in range(2):
                player.add_card(self.deck.deal())
                self.cards_dealt += 1
        for _ in range(2):
            self.dealer.add_card(self.deck.deal())
            self.cards_dealt += 1
        if self.cards_dealt >= marker_position:
            self.cut_card_reached = True

    def player_bets(self):
        """Get the player's bets."""
        self.dealer.reset_player()
        self.num_players_busted = 0
        for player in self.players:
            player.reset_player()
            if player.get_money() == 0:
                print(
                    "An anonymous donor has given $10,000 to "
                    + player.get_name()
                    + "!"
                )
                player.set_money(10000)
            print("=============================================")
            print(
                player.get_name()
                + "'s current balance: $"
                + str(player.get_money())
            )
            print("=============================================")

            while True:
                print("How much would you like to bet? ")
                try:
                    bet_value = int(input())
                except ValueError:
                    print("Please enter a number!")
                    continue
                if 0 < bet_value <= player.get_money():
                    player.set_bet(bet_value)
                    break
                if bet_value > player.get_money():
                    print("You do not have enough money to bet that much!")
                    break
                print("Please enter a number greater than 0!")

            print(
                "Player: "
                + player.get_name()
                + "\nBet Amount: "
                + str(player.get_bet())
            )
        print("\n\n")

    def player_turn(self, player, dealer):
        """Handle the player's turn."""
        double_down_prompt = True
        while player.get_hit():
            print("=============================================")
            print("CURRENT PLAYER: " + player.get_name().center(40))
            print("=============================================")
            print("Dealer's Hand:")
            format_hand(dealer.get_hand(), True)
            print(player.get_name() + "'s Hand:")
            format_hand(player.get_hand())
            print("Hand Value: " + str(sum_hand(player.get_hand())) + "\n")
            if (
                player.get_money() >= player.get_bet() * 2
                and double_down_prompt
            ):
                print("Would you like to double down?(Y/N) ")
                if input().upper() == "Y":
                    player.set_bet(player.get_bet() * 2)
                    player.add_card(self.deck.deal())
                    self.cards_dealt += 1
                    print(player.get_name() + " doubles down!\n\n")
                    player.set_hit(False)
                    format_hand(player.get_hand())
                    print(
                        "Hand Value: " + str(sum_hand(player.get_hand())) + "\n"
                    )
                    if sum_hand(player.get_hand()) > 21:
                        print("Player: " + player.get_name() + " busted!")
                        player.set_bust(True)
                        self.num_players_busted += 1
                        player.set_money(player.get_money() - player.get_bet())
                        break
                    if sum_hand(player.get_hand()) == 21:
                        print(
                            "Player: " + player.get_name() + " has blackjack!"
                        )
                        break
            double_down_prompt = False
            if sum_hand(player.get_hand()) > 21:
                print("Player: " + player.get_name() + " busted!")
                player.set_bust(True)
                self.num_players_busted += 1
                player.set_money(player.get_money() - player.get_bet())
                break
            if sum_hand(player.get_hand()) == 21:
                print("Player: " + player.get_name() + " has blackjack!")
                break
            print("Would you like to hit or stand?(H/S) ")
            if input().upper() == "H":
                player.set_hit(True)
                print("Player: " + player.get_name() + " hits!\n\n")
            else:
                player.set_hit(False)
                print("Player: " + player.get_name() + " stands!\n\n")
                break
            if player.get_hit():
                player.add_card(self.deck.deal())

    def dealer_blackjack(self, dealer):
        """Handle the dealer's blackjack."""
        print("=============================================")
        print("DEALER'S TURN".center(40))
        print("=============================================")
        print("Dealer has blackjack!")
        print("Dealer's Hand:")
        format_hand(dealer.get_hand())
        print("Hand Value: " + str(sum_hand(dealer.get_hand())) + "\n")
        for player in self.players:
            if sum_hand(player.get_hand()) == 21:
                print("Player: " + player.get_name() + " pushes!")
            else:
                player.set_money(player.get_money() - player.get_bet())
                print("Player: " + player.get_name() + " loses!")

    def dealer_busts(self, dealer):
        """Handle the dealer busting."""
        print("=============================================")
        print("DEALER'S TURN".center(40))
        print("=============================================")
        print("Dealer busts!")
        print("Dealer's Hand:")
        format_hand(dealer.get_hand())
        print("Hand Value: " + str(sum_hand(dealer.get_hand())) + "\n")
        for player in self.players:
            if player.get_bust():
                print("Player: " + player.get_name() + " loses!")
                player.set_money(player.get_money() - player.get_bet())
            else:
                print("Player: " + player.get_name() + " wins!")
                player.set_money(player.get_money() + player.get_bet())

    def dealer_stands(self, dealer):
        """Handle the dealer standing."""
        print("=============================================")
        print("DEALER'S TURN".center(40))
        print("=============================================")
        print("Dealer stands!")
        print("Dealer's Hand:")
        format_hand(dealer.get_hand())
        print("Hand Value: " + str(sum_hand(dealer.get_hand())) + "\n")
        for player in self.players:
            if player.get_bust():
                print("Player: " + player.get_name() + " loses!")
                player.set_money(player.get_money() - player.get_bet())
            elif sum_hand(player.get_hand()) > sum_hand(dealer.get_hand()):
                print("Player: " + player.get_name() + " wins!")
                player.set_money(player.get_money() + player.get_bet())
            elif sum_hand(player.get_hand()) < sum_hand(dealer.get_hand()):
                print("Player: " + player.get_name() + " loses!")
                player.set_money(player.get_money() - player.get_bet())
            else:
                print("Player: " + player.get_name() + " pushes!")

    def dealer_bust(self, dealer):
        """Handle the dealer's bust."""
        print("=============================================")
        print("DEALER'S TURN".center(40))
        print("=============================================")
        print("Dealer busted!")
        print("Dealer's Hand:")
        format_hand(dealer.get_hand())
        print("Hand Value: " + str(sum_hand(dealer.get_hand())) + "\n")
        for player in self.players:
            if not player.get_bust():
                player.set_money(player.get_money() + player.get_bet())
                print("Player: " + player.get_name() + " wins!")

    def dealer_turn(self, dealer):
        """Handle the dealer's turn."""
        print("=============================================")
        print("DEALER'S TURN".center(40))
        print("=============================================")
        dealer_hand = dealer.get_hand()
        dealer_hand_value = sum_hand(dealer_hand)
        print("Dealer's Hand:")
        format_hand(dealer_hand)
        print("Hand Value: " + str(dealer_hand_value) + "\n")
        if self.num_players_busted == self.num_players:
            print("Dealer wins!, all players busted!")
        else:
            while dealer_hand_value < 17:
                dealer.add_card(self.deck.deal())
                print("Dealer hits!")
                format_hand(dealer_hand)
                dealer_hand = dealer.get_hand()
                dealer_hand_value = sum_hand(dealer_hand)

            if sum_hand(dealer_hand) > 21:
                self.dealer_busts(dealer)
            elif dealer_hand_value == 21:
                self.dealer_blackjack(dealer)
            else:
                self.dealer_stands(dealer)
        print("\n")

    def pickle_players(self):
        """Pickle the players list to a file."""
        if not os.path.exists("data"):
            os.makedirs("data")
        with open("data/players.pickle", "wb") as pick_file:
            pickle.dump(self.players, pick_file)
        print("Players saved!")

    def unpickle_players(self):
        """Unpickle the players list from a file."""
        if os.path.exists("data/players.pickle"):
            with open("data/players.pickle", "rb") as pick_file:
                self.players = pickle.load(pick_file)
            print("Players loaded!")
            for player in self.players:
                print(
                    "Player: "
                    + player.get_name()
                    + " Money: "
                    + str(player.get_money())
                )


def init_game():
    """Initialize the game."""
    num_decks = 8
    print("Welcome to Blackjack!")
    print("Would you like to load a previous game? (Y/N) ")
    if input().upper() == "Y":
        if os.path.exists("data/players.pickle"):
            blackjack_game = Game(0, num_decks)
            blackjack_game.unpickle_players()
            blackjack_game.num_players = len(blackjack_game.players)
            blackjack_game.deck.shuffle()
            blackjack_game.deck.cut()
            return blackjack_game
        print("No previous game found!")

    print("Starting new game!\n")
    while True:
        print("How many players are playing? ")
        # check if input is an integer
        try:
            num_players = int(input())
        except ValueError:
            print("Please enter a number!")
            continue
        if 0 < num_players <= 7:
            break
        print("Please enter a number greater than 0! (Max 7)")

    blackjack_game = Game(num_players, num_decks)
    blackjack_game.deck.shuffle()
    blackjack_game.deck.cut()
    return blackjack_game


def main_game_loop():
    """Main game loop."""
    blackjack_game = init_game()

    while True:
        blackjack_game.player_bets()
        blackjack_game.deal_cards()
        for player in blackjack_game.players:
            blackjack_game.player_turn(player, blackjack_game.dealer)
        blackjack_game.dealer_turn(blackjack_game.dealer)
        if blackjack_game.cut_card_reached:
            blackjack_game.deck.shuffle()
            blackjack_game.cut_card_reached = False
            blackjack_game.cards_dealt = 0
        for player in blackjack_game.players:
            print(
                "Player: "
                + player.get_name()
                + " Money: "
                + str(player.get_money())
            )
        print("Would you like to play again?(Y/N) ")
        if input().upper() == "Y":
            continue
        print(
            "Would you like to save your game?"
            + " This will overwrite any previous save files. (Y/N) "
        )
        if input().upper() == "Y":
            blackjack_game.pickle_players()
            print("Saved Game!")
        else:
            print("Exiting without saving...")
        break
