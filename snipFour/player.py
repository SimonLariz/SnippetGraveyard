
class Player:
    def __init__(self, name, money=10000):
        self.name = name
        self.money = money
        self.hands = []
        self.bet = 0
        self.bust = False
        self.blackjack = False
        self.hit = True

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def get_bet(self):
        return self.bet

    def get_hands(self):
        return self.hands

    def set_money(self, money):
        self.money = money

    def set_bet(self, bet):
        self.bet = bet

    def set_hands(self, hands):
        self.hands = hands

    def add_hand(self, hand):
        self.hands.append(hand)

    def add_card(self, card):
        self.hands[-1].append(card)

    def get_hit(self):
        return self.hit

    def set_hit(self, hit):
        self.hit = hit

    def get_bust(self):
        return self.bust

    def reset_player(self):
        self.hands = []
        self.bet = 0
        self.bust = False
        self.blackjack = False
        self.hit = True
