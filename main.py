"""Password Manager Main file"""
from tkinter import *
# pyperclip helps to put out password into our clipboard so we can easily paste it elsewhere
import pyperclip
# Import message box from tkinter as line 2 * doesnt import message box which is a seperate module of code
from tkinter import messagebox
# Passwords are going to be saved in a json file
import json
# password generator
from password_generator import password_generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    # Generate new password from password generator
    password = password_generator()
    # Copying password to our clipboard
    pyperclip.copy(password)
    # clear password entry widget
    password_entry.delete(0, END)
    # entering new password to password entry widget
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # getting user entry data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Dialog to user to make sure password is correct
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm entries", message=f"These are the details you entered\n"
                                                                        f"Email: {email}"
                                                                        f"\nPassword: {password}\nIs it okay to save")
        if is_ok:
            # copying password to our clipboard
            pyperclip.copy(password)
            # new user data to be entered into current password data file as json
            new_entry_json_data = {
                website:
                    {
                        email: email,
                        password: password
                    }
            }
            try:
                # seeing if there is any old passwords data file
                with open("data.json", mode="r") as old_password_file:
                    # reading old password data
                    password_data = json.load(old_password_file)
            # if there is no file or if there is a file but no entries in it:
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", mode="w") as new_password_file:
                    json.dump(new_entry_json_data, new_password_file, indent= 4)
            # if there is old password data,
            else:
                #  New user entry json data will be updated to the old passwords data
                password_data.update(new_entry_json_data)
                # Writing either the updated password data or the new user entry json data in current_password_data
                with open("data.json", mode="w") as old_password_file:
                    json.dump(password_data, old_password_file, indent=4)
            finally:
                # finally , we are clearing website and password entry fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# New tkinter Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# ---------------------------- WIDGETS SETUP ------------------------------- #
# canvas widget
PASS_IMG = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.config()
canvas.create_image(100, 100, image=PASS_IMG)
canvas.grid(column=1, row=0)

# Label
# Label for Website
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

# Label for Email/Username
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

# Label for Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
window.grid_columnconfigure(1, weight=1)
# Entry widgets
website_entry = Entry(width=38)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1, columnspan=2)
# starting cursor focus
website_entry.focus()

email_entry = Entry(width=38)
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2, columnspan=2)
# set default email
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=38)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3, columnspan=2)

# buttons
generate_button = Button(text="Generate Password", command=get_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
