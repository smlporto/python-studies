alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):

    #Shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    encrypted_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > len(alphabet):
            new_position = (new_position - len(alphabet))
        encrypted_text += alphabet[new_position]
        
    print(f"Encrypted text: {encrypted_text}")

#Call the encrypt function
encrypt(text, shift)