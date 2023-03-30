import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        letters_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters allowed.")
        generate_phonetic()
    else:
        print(letters_list)

generate_phonetic()