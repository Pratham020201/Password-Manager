import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
 # ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
        password_entry.insert( 0 , password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email =email_username_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
  else:
      to_save = messagebox.askokcancel(title=website , message=f"These are the details entered: \n"
                                                               f"Email: {email} \nPassword: {password} \nAre the details correct?")
      if to_save:
        with open("data.txt" , "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0 , END)
            password_entry.delete(0 , END)




# ---------------------------- UI SETUP ------------------------------- #

window =tkinter.Tk()
window.title("Password Manager")
window.config(pady=50 , padx=50)

canvas = Canvas( height=200 , width=200 )
Logo = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image = Logo)
canvas.grid(row=0 , column=1)

website_label = Label(text="Website:")
website_label.grid(row=1 ,column=0)

email_username_label = Label(text="Email/Username :")
email_username_label.grid(row=2 , column=0)

password_label = Label(text = "Password :")
password_label.grid(row=3 , column=0 , )

website_entry = Entry( width=55)
website_entry.grid(row=1 , column=1 , columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=55)
email_username_entry.grid(row=2, column=1 , columnspan=2)
email_username_entry.insert(0 , "prathameshpalande020201@gmail.com")

password_entry=Entry(width=35)
password_entry.grid(row=3 , column=1 )

GENERATE_PASSWORD_BUTTON=Button(text="Generate Password" , width=16 , command=password_generator)
GENERATE_PASSWORD_BUTTON.grid(row=3 , column=2)

ADD_BUTTON =Button(text="Add" , width=46 , command=save)
ADD_BUTTON.grid(row=4 , column=1 , columnspan=2)









window.mainloop()
