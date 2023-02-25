from cards import *
from player import *


class Game:
    def __init__(self, num_players, num_decks):
        self.deck = FrenchDeck(num_decks)
        self.num_players = num_players
        self.players = []
        for x in range(num_players):
            player_name = input("What is player " + str(x + 1) + "'s name? ")
            self.players.append(Player(player_name))
        self.dealer = Player("DEALER")
        self.turn_number = 0
        self.num_players_busted = 0
        self.marker = self.deck._marker
        self.cards_dealt = 0
        self.cut_card_reached = False


def init_Game():
    global myBlackjackGame
    print("Welcome to Blackjack!")
    print("How many players are playing? ")
    num_players = int(input())
    num_decks = 8
    myBlackjackGame = Game(num_players, num_decks)
    myBlackjackGame.deck.shuffle()
    myBlackjackGame.deck.cut()


def player_bets():
    myBlackjackGame.dealer.reset_player()
    for player in myBlackjackGame.players:
        player.reset_player()
        print("Player: " + player.get_name() +
              " Money: " + str(player.get_money()))
        print("How much would you like to bet? ")
        player_bet = int(input())
        while player_bet > player.get_money():
            print("You do not have enough money to bet that much!")
            print("How much would you like to bet? ")
            player_bet = int(input())
        player.set_bet(player_bet)
        print("Player: " + player.get_name() +
              "\nBet Amount: " + str(player.get_bet()))
    print("\n\n")


def deal_cards():
    for player in myBlackjackGame.players:
        player.add_hand([])
        for x in range(2):
            player.add_card(myBlackjackGame.deck.deal())
            myBlackjackGame.cards_dealt += 1
    myBlackjackGame.dealer.add_hand([])
    for x in range(2):
        myBlackjackGame.dealer.add_card(myBlackjackGame.deck.deal())
        myBlackjackGame.cards_dealt += 1
    if myBlackjackGame.cards_dealt >= myBlackjackGame.marker:
        myBlackjackGame.cut_card_reached = True


def player_turn(player, dealer):
    print("=============================================")
    print("CURRENT PLAYER: " + player.get_name().upper().center(40))
    print("=============================================")
    while player.get_hit():
        display_table(player, dealer)
        if sum_hand(player.get_hands()[-1]) > 21:
            print("Player: " + player.get_name() + " busted!")
            player.set_money(player.get_money() - player.get_bet())
            break
        elif sum_hand(player.get_hands()[-1]) == 21:
            print("Player: " + player.get_name() + " has blackjack!")
            player.set_money(player.get_money() + player.get_bet())
            break
        else:
            print("Would you like to hit or stand?(H/S) ")
            player_selection = input()
            if player_selection == "H" or player_selection == "h":
                player.set_hit(True)
                print("Player: " + player.get_name() + " hits!\n\n")
            else:
                player.set_hit(False)
                print("Player: " + player.get_name() + " stands!\n\n")
                break
            if player.get_hit():
                player.add_card(myBlackjackGame.deck.deal())


def dealer_turn(dealer):
    display_dealer_hand(dealer)
    while sum_hand(dealer.get_hands()[-1]) < 17:
        dealer.add_card(myBlackjackGame.deck.deal())
        print("Dealer hits!")
        display_dealer_hand(dealer)
    if sum_hand(dealer.get_hands()[-1]) > 21:
        print("Dealer busted!")
        for player in myBlackjackGame.players:
            if not player.get_bust():
                player.set_money(player.get_money() + player.get_bet())
                print("Player: " + player.get_name() + " wins!")
    elif sum_hand(dealer.get_hands()[-1]) == 21:
        print("Dealer has blackjack!")
        for player in myBlackjackGame.players:
            if not player.get_bust():
                player.set_money(player.get_money() - player.get_bet())
                print("Player: " + player.get_name() + " loses!")
    else:
        for player in myBlackjackGame.players:
            if not player.get_bust():
                if sum_hand(player.get_hands()[-1]) > sum_hand(dealer.get_hands()[-1]):
                    player.set_money(player.get_money() + player.get_bet())
                    print("Player: " + player.get_name() + " wins!")
                elif sum_hand(player.get_hands()[-1]) < sum_hand(dealer.get_hands()[-1]):
                    player.set_money(player.get_money() - player.get_bet())
                    print("Player: " + player.get_name() + " loses!")
                else:
                    print("Player: " + player.get_name() + " pushes!")

    print("\n\n")


def display_table(player, dealer):
    print("Dealer hand:")
    for hand in dealer.get_hands():
        for card in hand:
            print(str(card))
        print("Hand Value: " + str(sum_hand(hand)))
    print("--------------------\n")
    print("Player: " + player.get_name() + " hand: ")
    for hand in player.get_hands():
        for card in hand:
            print(str(card))
        print("Hand Value: " + str(sum_hand(hand)))
        print("--------------------\n")


def display_dealer_hand(dealer):
    print("Dealer hand:")
    for hand in dealer.get_hands():
        for card in hand:
            print(str(card))
        print("Hand Value: " + str(sum_hand(hand)))
    print("--------------------\n")


def main_game_loop():
    init_Game()
    while True:
        player_bets()
        deal_cards()
        for player in myBlackjackGame.players:
            player_turn(player, myBlackjackGame.dealer)
        dealer_turn(myBlackjackGame.dealer)
        if myBlackjackGame.cut_card_reached:
            myBlackjackGame.deck.shuffle()
            myBlackjackGame.cut_card_reached = False
            myBlackjackGame.cards_dealt = 0
        for player in myBlackjackGame.players:
            print("Player: " + player.get_name() +
                  " Money: " + str(player.get_money()))
        print("Would you like to play again?(Y/N) ")
        play_again = input()
        if play_again == "Y" or play_again == "y":
            continue
        else:
            break


main_game_loop()
