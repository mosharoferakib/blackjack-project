import random
import colorama 
from colorama import Fore

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(1, 13):
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 1 and self.value + 11 <= 21:
            self.value += 11
        elif card.rank >= 10:
            self.value += 10
        else:
            self.value += card.rank
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    
    def play(self):
        print(Fore.RED + "Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(Fore.GREEN + f"Dealer's hand: \n {self.dealer_hand.cards[0]}, hidden card")
        print(Fore.BLUE + f"Your hand: \n {self.player_hand}")
        while True:
            action = input(Fore.YELLOW + "Do you want to hit or stand? ")
            if action.lower() == "hit":
                self.player_hand.add_card(self.deck.deal_card())
                print(Fore.BLUE + f"Your hand: \n {self.player_hand}")
                if self.player_hand.value > 21:
                    print(Fore.GREEN + "You bust! Dealer wins.")
                    return
            elif action.lower() == "stand":
                break
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        print(Fore.GREEN + f"Dealer's hand: \n {self.dealer_hand}")
        if self.dealer_hand.value > 21:
            print(Fore.BLUE + "Dealer busts! You win!!!")
        elif self.dealer_hand.value > self.player_hand.value:
            print(Fore.GREEN + "Dealer wins.")
        elif self.dealer_hand.value < self.player_hand.value:
            print(Fore.YELLOW + "!!!You win!!!")
        else:
            print(Fore.YELLOW + "It's a tie.")


blackjack = Blackjack()
blackjack.play()