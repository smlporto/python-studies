from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = input_website.get()
    email_username = input_email_username.get()
    password = input_password.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!!")
    else:
        is_ok =messagebox.askokcancel(title=f"Password for {website}", message=f"Are you sure?\nEmail: {email_username}\nPassword: {password}")

        if is_ok:
            with open("passwords.txt", "a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
        
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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(width=36, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()