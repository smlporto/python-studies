#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", "r") as guest_list:
    names = guest_list.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as start_letter:
    text = start_letter.read()

    for name in names:
        clean_name = name.strip()
        edited_text = text.replace("[name]", clean_name)

        with open(f"./Output/ReadyToSend/{clean_name}.txt", "x") as final_letter:
            final_letter.write(edited_text)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp