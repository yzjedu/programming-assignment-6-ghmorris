import random

# Programmer: Grace-Ann Morris 
# Course: CS701/GB-731, Dr. Yalew
# Date: August 24, 2024 
# Programming Assignment: 6 'A Simiplified Blackjack Game'

#Function that creates a shuffled deck of 52 cards.
def generate_deck():
    suits = ['h', 'd', 'c', 's']  #Speciality Cards: Hearts, Diamonds, Clubs, Spades
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']  #1=Ace, 11=Jack, 12=Queen, 13=King
    deck = [f'{rank}{suit}' for suit in suits for rank in ranks] #Create all combinations of rank and suit
    random.shuffle(deck) #Shuffle the deck
    return deck

#Function that returns the name of a card given its string representation.
def card_name(card):
    rank_map = {'1': 'Ace', '11': 'Jack', '12': 'Queen', '13': 'King'}
    suits = {'h': 'Hearts', 'd': 'Diamonds', 'c': 'Clubs', 's': 'Spades'}
    rank = card[:-1]  #Retrieve rank from card string
    suit = card[-1]   #Retrieve suit from card string
    rank_name = rank_map.get(rank, rank) #Map rank to name/use rank as is
    suit_name = suits.get(suit, suit) #Map suit to name/use suit as is
    
    return f'{rank_name} of {suit_name}'

#Function that displays the names of the cards in a hand.
def display_hand(hand):
    return ', '.join(card_name(card) for card in hand)

#Function that calculates and returns the total value of a hand.
def hand_value(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              '11': 10, '12': 10, '13': 10}
    total = 0
    aces = 0
    for card in hand:
        rank = card[:-1]  #Get rank from card string
        if rank == '1':  #Ace
            aces += 1
            total += 11
        else:
            total += values.get(rank, 0)
    #Adjust for Aces if necessary
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def main():
    deck = generate_deck()
    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print("Welcome to Simplified Blackjack!")
    
    # User's turn
    while True:
        print(f"Your hand: {display_hand(user_hand)}")
        print(f"Your hand value: {hand_value(user_hand)}")
        
        if hand_value(user_hand) > 21:
            print("You bust! Dealer wins.")
            return
        action = input("Would you like to (h)it or (s)tand? ").lower()
        if action == 'h':
            user_hand.append(deck.pop())
        elif action == 's':
            break
        else:
            print("Invalid input. Please choose 'h' or 's'.")
    
    #Dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    print(f"Dealer's hand: {display_hand(dealer_hand)}")
    print(f"Dealer's hand value: {hand_value(dealer_hand)}")
    
    #Determine the winner
    user_score = hand_value(user_hand)
    dealer_score = hand_value(dealer_hand)
    
    if dealer_score > 21 or user_score > dealer_score:
        print("You win!")
    elif user_score < dealer_score:
        print("Dealer wins")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
