from art import logo
from random import randint

def sort_number():
	"""Sort a random number"""
	correct_number = randint(1, 100)
	return correct_number

def set_difficulty(chosen_difficulty):
	"""Defines the game number of lives the player will have"""
	if chosen_difficulty == "hard":
		return 5
	else:
		return 10

def verify_answer(current_guess, answer):
	"""Compares the guess with the real answer"""
	if current_guess > answer:
		print("Too high.")
	elif current_guess < answer:
		print("Too Low.")
	else:
		print(f"\nCongrats!! You got it right!\nThe answer was {answer}.")

def guess_game():
	print(logo)
	print("I'm thinking of a number between 1 and 100.\nCan you guess it right?")
	
	difficulty = input("\nChoose dificulty ('easy' or 'hard'): ")
	attempts = set_difficulty(difficulty)
	answer = sort_number()
	guess = 0
	
	while guess != answer:
		guess = int(input("\nGuess a number: "))
		
		attempts -= 1
		print(f"You have {attempts} remaining attempts.")

		verify_answer(guess, answer)

		if attempts == 0:
			print("\nYou run out of attempts!\nGame Over.")
			return

guess_game()