from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_lowercase_letters = random.randint(4,8)
    nr_uppercase_letters = random.randint(1,2)
    nr_symbols = random.randint(1,4)
    nr_numbers = random.randint(2,4)

    password_list = []

    password_lowercase_letters = [random.choice(lowercase_letters) for _ in range(nr_lowercase_letters)]
    password_uppercase_letters = [random.choice(uppercase_letters) for _ in range(nr_uppercase_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_uppercase_letters + password_lowercase_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    pyperclip.copy

    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = input_website.get()
    email_username = input_email_username.get()
    password = input_password.get()
    new_data = {website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!!")
    else:
        try:
            with open("password_manager.json", "r") as json_data:
                #Reading old data
                data = json.load(json_data)
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:
            with open("password_manager.json", "w") as json_data:
                #Saving updated data
                json.dump(data, json_data, indent=4)
        
            input_website.delete(0, END)
            input_email_username.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_website.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

input_email_username = Entry(width=35)
input_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(width=36, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()