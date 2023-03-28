import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()

letters_list = [nato_dict[letter] for letter in word]
print(letters_list)