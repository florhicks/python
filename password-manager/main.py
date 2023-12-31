from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Search password
def search_password():
    try:
         with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error",message="File not found, make an entry")
    else:
        website= input_website.get()
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f" \nEmail/Username: {data[website]["email"]}\n"
                                                                   f"Password: {data[website]["password"]}\n")
        else:
            messagebox.showinfo(title=f"{website} information not found", message="No details for the website exists")
# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password_gen = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password_gen)

    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    username = input_email_username.get()
    password = input_password.get()
    new_data = {website: {
        "email": username,
        "password": password
    }}

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please, dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:"
                                                                   f" \nEmail/Username: {username}\n"
                                                                   f"Password: {password}\nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # file.write(f"{website} | {username} | {password} \n")
                input_password.delete(0, END)
                input_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=4)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2, pady=4)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=4)

# Entries
input_website = Entry(width=34)
input_website.grid(column=1, row=1, pady=4)
input_website.focus()

input_email_username = Entry(width=55)
input_email_username.grid(column=1, row=2, columnspan=2, pady=4)
input_email_username.insert(0, "user@email.com")

input_password = Entry(width=34)
input_password.grid(column=1, row=3, pady=4)

# Buttons
button_generate = Button(text="Generate Password", width=16, command=password_generator)
button_generate.grid(column=2, row=3, pady=4)
button_add = Button(text="Add", width=46, command=save)
button_add.grid(column=1, row=4, columnspan=2, pady=4)
button_search= Button(text="Search",width=16,command=search_password)
button_search.grid(column=2, row=1)

window.mainloop()
