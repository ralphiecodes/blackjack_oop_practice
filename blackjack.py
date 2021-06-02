import random

#Suits of Cards
suits =('Hearts', 'Diamonds', "Spades", "Clubs")
#Ranks of Cards
ranks = ('Two', 'Three', 'Four', 'Five', "Six", 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#Dictionary of Ranks and the values associated with them
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace' : 14}
playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return "Deck has " + deck_comp

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 11
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100 
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please place your bet: '))
        except ValueError:
            print('That is not a correct value. Try Again')
        else:
            if chips.bet > chips.total:
                print('You cannot place a bet that exceeds the amount of your chips ' + str(chips.total))
            else:
                break   

def hit(deck,hand):
        
        hand.add_card(deck.deal())  
        hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    player_input = input('Would you like to hit or stand? enter h or s ')
    while playing:
        if player_input.lower() == 'h':
            hit(deck,hand)
        elif player_input.lower() == 's':
            playing = False
        else:
            print('Try again ')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.lose_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins!')
    chips.win_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
   
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
  
    player_chips = Chips()   
    
    
    take_bet(player_chips)
    
    
    show_some(player_hand,dealer_hand)
    
    while playing:  
        
        
        hit_or_stand(deck,player_hand) 
        
       
        show_some(player_hand,dealer_hand)  
        

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
      
        show_all(player_hand,dealer_hand)
     
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break