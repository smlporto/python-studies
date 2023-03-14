from random import randint
from art import logo, vs
from game_data import data
import os

def random_index():
    """generate random index based on data length"""
    return randint(0, len(data) - 1)

def higher(option_a, option_b):
    """Compare the data to find the one with more followers"""
    if data[option_a]['follower_count'] > data[option_b]['follower_count']:
        return 'A'
    else:
        return 'B'
    
def compare_answer(user_choice, correct_choice, score):
    """Check if the answer is right and show the score"""
    if user_choice == correct_choice:
        print(f"Congrats! You got it. | Score: {score}\n")
    else:
        print(f"Oh oh, that's wrong! | Final score: {score}\n")
        play_again = input("Play again? ('y' or 'n'): ").upper()
        if play_again == 'Y':
            os.system('cls')
            higher_lower()

def higher_lower():

    #display game logo
    print(logo)

    #generate random index number that are different from each other
    a = 0
    b = 0

    while a == b:
        a = random_index()
        b = random_index()
    
    #initiate variables for the game
    answer = ''
    right_choice = ''
    score = 0
    
    while answer == right_choice:
        #display first item in the game_data dictionary
        print(f"A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")

        # #display "vs" logo
        print(vs)

        #display second item in game_data, different from the first one
        print(f"B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")

        #compare follower count from first to second item
        right_choice = higher(a, b)

        #Input from the user with the answer
        answer = input(f"\nWho has more followers? ('A' or 'B'): ").upper()

        #Sum to the total score
        if answer == right_choice:
            score += 1
        
        if answer == 'A':
            b = random_index()
        else: 
            a = b
            b = random_index()

        os.system('cls')

        #Check answer and print result and score
        compare_answer(answer, right_choice, score)

higher_lower()