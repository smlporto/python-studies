#Step 5
import os
import random
import hangman_art
import hangman_words

#Choose a random word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Defines the number of lives the player has and the end of the game.
end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guesses = []

#Create blanks for each letter in the chosen_word.
for _ in range(word_length):
    display += "_"

#Loop until the end of the lives or the discovery of the word.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clearing the Screen
    os.system('cls')

    #Tells if the user has entered a letter they've already guessed
    if guess in guesses:
      print("You have already guessed this letter!")
    else: 
      guesses.append(guess)
			
    print(f"Already used letters: {', '.join(guesses).upper()}\n")
			
    #Check guessed letter and replace the blanks with the correct letter.
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, remove one of his lives and let them know the letter it's not in the word.
        lives -= 1
        print("This letter is not in the word!")
			
        #If the user has no more lives, the game ends.
        if lives == 0:
            end_of_game = True
            print("\nYou lose!!")
            print(f"The word was {chosen_word}.\n")

    #Join all the letters in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win!!")

    #Import the stages of the hangman from hangman_art.py and make it print the right stage depending on the user's lives.
    print(hangman_art.stages[lives])