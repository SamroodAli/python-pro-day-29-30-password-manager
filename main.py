"""Password Manager Main file"""

# ---------------------------- IMPORTS------------------------------- #
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
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
website_entry = Entry(width=35)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1, columnspan=2)


email_entry = Entry()
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2)

password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

# buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
