"""Password Manager Main file"""

# ---------------------------- IMPORTS------------------------------- #
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("data.txt", mode="a") as password_file:
        website = website_entry.get()
        website_entry.delete(0, END)
        email = email_entry.get()
        email_entry.delete(0, END)
        password = password_entry.get()
        password_entry.delete(0, END)
        password_file.write(f"{website},{email},{password}\n")


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
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
