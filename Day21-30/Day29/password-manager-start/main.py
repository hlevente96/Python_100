from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- CONSTANTS  ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    entry3.delete(0, END)
    password_list = []
    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    line = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error - Empty Box",
            message="You have left something empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title="Add New Password",
            message=f"These are the details entered:\n"
                    f"Website: {website}\n"
                    f"Email: {email}\n"
                    f"Password: {password}\n"
                    f"Is it okay to save?"
        )
        if is_ok:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            entry1.delete(0,END)
            entry3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200,width=200)
# Image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)
# Labels
label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)
# Entries
entry1 = Entry(width=40)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()
entry2 = Entry(width=40)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0,"test123@gmail.com")
entry3 = Entry(width=22)
entry3.grid(row=3, column=1)
# Button
button_generate = Button(
    text="Generate Password",
    highlightthickness=0,
    command=generate
)
button_generate.grid(row=3, column=2)
button_add = Button(
    text="Add",
    width=38,
    command=save_password
)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()