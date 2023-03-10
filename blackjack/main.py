import random
import os
from art import logo

def deal_card(): 
    """Return random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else: 
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
def find_winner(player, computer):
    if computer == player:
        return "Draw"
    elif computer == 0:
        return "You Lose. Computer has a Blackjack!"
    elif player == 0:
        return "You Win!! You have a Blackjack!"
    elif player > 21:
        return "You went over. You Lose!"
    elif computer > 21:
        return "Computer went over. You Win!!"
    elif player > computer:
        return "You Win!!"
    else:
        return "You Win!!"

def blackjack():
    print(logo)

    #Initialize player and computer cards
    player_cards = []
    computer_cards = []

    #Distribute 2 random initial cards for player and computer
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:

        #Calculate the scores for player and computer
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYou cards: {player_cards} | Score: {player_score}")
        print(f"Computer card: {computer_cards[0]}")

        #Verify if someone win, lose or want to keep playing
        if player_score == 0 or computer_score == 21 or player_score > 21:
            game_over = True
        else:
            answer = input("Do you want another card? ('y' or 'n') ")
            if answer == "y":
                player_cards.append(deal_card())
            else: 
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYou cards: {player_cards} | Score: {player_score}")
    print(f"Computer cards: {computer_cards} | Score: {computer_score}")
    print("\n**************************\n" + find_winner(player_score, computer_score) + "\n**************************")

print(logo)
while input("################## Start game? ('y' or 'n') ##################\n") == 'y':
    os.system('cls')
    blackjack()
    