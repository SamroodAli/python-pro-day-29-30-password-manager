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
label = Label(text="Website")
label.grid(column=0, row=1)

# Label for Email/Username
label = Label(text="Email/Username")
label.grid(column=0, row=2)

# Label for Password
label = Label(text="Password")
label.grid(column=0, row=3)
















window.mainloop()
