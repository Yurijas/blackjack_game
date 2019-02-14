#TODO?: 1. make dealer be able to choose stay :dealer_total > 16: random.choice(hand)??
#TODO?: 2. make card_suit = ['Hearts','Spades','Clubs','Diamonds']
#TODO?: 3. define when it's close enough to 21 but not yet and player wins/loses??

# output() function
from IPython.display import clear_output
# get random word from the word list
import random
# **********
# ** card **
# **********
# cards (J,Q,K = 10, A = 11(or1))
card_value = [
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
            ]

# **********************
# ** Dealer & Player  **
# ******take turns******
# while game's on
class Blackjack():
    def __init__(self):
        # dealer cards
        self.dealer_deck = []
        self.dealer_total = 0
        # player cards
        self.player_deck = []
        self.player_total = 0

    # dealer hand
    def calcDealerHand(self):
        total = 0
        for card in self.dealer_deck:
            total += card
        self.dealer_total = total
        # for ACE
        for card in self.dealer_deck:
            if card == 11 and self.dealer_total > 21:
                self.dealer_total -= 10
    # player hand
    def calcPlayerHand(self):
        total = 0
        for card in self.player_deck:
            total += card
        self.player_total = total
        # for ACE
        for card in self.player_deck:
            if card == 11 and self.player_total > 21:
                self.player_total -= 10

    def printHands(self):
        print('Dealer: {}'.format(self.dealer_deck))
        print('Player: {}'.format(self.player_deck))

    # give 2 cards at first
    def dealCards(self):
        for i in range(2):
            self.dealer_deck.append(random.choice(card_value))
            self.player_deck.append(random.choice(card_value))
            self.printHands()

    # dealer gets card
    def dealerMove(self):
        self.calcDealerHand()
        while self.dealer_total < 18:
            self.dealer_deck.append(random.choice(card_value))
            self.calcDealerHand()
            print("Dealer: {}".format(self.dealer_deck))
            print("Dealer's total is {}".format(self.dealer_total))

    # player gets card or does nothing
    def playerMove(self):
        while self.player_total < 22:
            ans = input("Please type your move: 'hit' or 'stay' ?")
            # player gets the card (hit)
            if ans.lower() == "hit":
                clear_output()
                self.player_deck.append(random.choice(card_value))
                print("Player: {}".format(self.player_deck))
                self.calcPlayerHand()
                print("Your total is {}".format(self.player_total))
            # player does nothing (stay)
            elif ans.lower() == "stay":
                clear_output()
                self.calcPlayerHand()
                print("Player: {}".format(self.player_deck))
                print("Your total is {}".format(self.player_total))
                break
            else:
                print("Sorry could you type again?")
                # break

    # *************
    # **condition** (total, player_total, dealer_total)
    # *************

    def gameCondition(self):
        # win
        if self.dealer_total>20 and self.player_total < self.dealer_total:
            print("Conglatuation! You won!")
        # lose
        elif self.player_total>20 and self.player_total > self.dealer_total:
            print("Sorry you lost and the dealer won.")
        # tie
        elif self.player_total<22 and self.player_total == self.dealer_total:
            print("Good game! The game is finished by being tie!")


# **********************
# **game start/finish**
# **********************
# game on/off
def gameSwitch():
    while True:
        ans = input("Please type 'start' or 'quit'.")
        # start
        if ans.lower() == "start":
            clear_output()
            game = Blackjack()

            # hand out cards
            game.dealCards()
            # ask player to stay or hit
            # if player goes over 21 busts and loses
            # when done, dealer hits until 17 or higher
            game.playerMove()
            # if dealer busts, player wins
            # if no bust, then check who has higher score

            if game.player_total <= 21:
                game.dealerMove()

            game.gameCondition()

            # repeat steps 1 through 6
        # quit
        elif ans.lower() == "quit":
            clear_output()
            print("Thank you for playing!")
            break
        else:
            print("Sorry could you type again?")



gameSwitch()
