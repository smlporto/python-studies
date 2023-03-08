from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > len(alphabet):
                new_position = new_position - len(alphabet)
            end_text += alphabet[new_position]

    print(f"Text {direction}d: {end_text}")

print(logo)


should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    answer = input(f"\nDo you want to do it again? ")

    if answer == "yes":
        should_continue = True
    else:
        should_continue = False

    