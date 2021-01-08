"""Password Manager Main file"""
from tkinter import *
# Import message box from tkinter
from tkinter import messagebox
# Passwords are going to be saved in a json file
import json
# pyperclip helps to put out password into our clipboard so we can easily paste it elsewhere
import pyperclip
# password generator
from password_generator import password_generator

# ---------------------------- UI COLORS AND FONT ------------------------------- #
WINDOW_BG = "#111d5e"
FIELD_COLORS = "#dddddd"
FIELD_FONT_COLOR = "#c70039"
LABEL_COLOR = "white"
FONT = ("Courier", 15, "normal")
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
def database_manager(new_user_entry):
    try:
        # seeing if there is any old passwords data file
        with open("data.json", mode="r") as old_password_file:
            # reading old password data
            password_data = json.load(old_password_file)
    # if there is no file or if there is a file but no entries in it:
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("data.json", mode="w") as new_password_file:
            json.dump(new_user_entry, new_password_file, indent=4)
    # if there is old password data,
    else:
        #  New user entry json data will be updated to the old passwords data
        password_data.update(new_user_entry)
        # Writing either the updated password data or the new user entry json data
        with open("data.json", mode="w") as old_password_file:
            json.dump(password_data, old_password_file, indent=4)
    finally:
        # finally , we are clearing website and password entry fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


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
            new_entry_in_json = {
                website:
                    {
                        email: email,
                        password: password
                    }
            }
            # Writing to the password database or updating it
            database_manager(new_entry_in_json)


# ---------------------------- UI SETUP ------------------------------- #
# New tkinter Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WINDOW_BG)

# ---------------------------- WIDGETS SETUP ------------------------------- #
# canvas widget
PASS_IMG = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=WINDOW_BG, highlightthickness=0)
canvas.config()
canvas.create_image(100, 100, image=PASS_IMG)
canvas.grid(column=1, row=0)

# Label
# Label for Website
website_label = Label(text="Website", bg=WINDOW_BG, padx=20, font=FONT, fg=LABEL_COLOR)
website_label.grid(column=0, row=1, sticky=W)

# Label for Email/Username
email_label = Label(text="Email/Username", bg=WINDOW_BG, padx=20, font=FONT, fg=LABEL_COLOR)
email_label.grid(column=0, row=2, sticky=W)

# Label for Password
password_label = Label(text="Password", bg=WINDOW_BG, padx=20, font=FONT, fg=LABEL_COLOR)
password_label.grid(column=0, row=3,sticky=W)
window.grid_columnconfigure(1, weight=1)
# Entry widgets
website_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)
# starting cursor focus
website_entry.focus()
email_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2)
# set default email
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

# buttons
search_button = Button(text="Search", command=get_password, padx=95, font=FONT)
search_button.grid(column=3, row=1)

generate_button = Button(text="Generate Password", command=get_password, font=FONT)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36, command=save_password, font=FONT)
add_button.grid(column=1, row=5, columnspan=2, sticky=W)

# Dummy widget for to get an empty rows
dummy_label = Label(bg=WINDOW_BG)
dummy_label.grid(column=0, row=4, sticky=W)

window.mainloop()

