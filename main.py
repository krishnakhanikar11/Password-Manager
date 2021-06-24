# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def pass_gen():
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

    pass_entry.insert(0,password)
    pyperclip.copy(password)



def file_create():
    website_name = website_entry.get()
    email_use = email_entry.get()
    pass_created= pass_entry.get()

    if len(website_name) == 0 or len(pass_created)==0:
        messagebox.showinfo(title="Empty Field", message="Don't leave and field empty")

    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                   message=f"These are the details you entered: \nEmail: {email_use} \n"
                                           f"Website: {website_name} \nPassword: {pass_created}")

        if is_ok:
            with open(f"./password-manager.txt", mode='a') as final:
                x = final.write(f"{website_name} | {email_use} | {pass_created}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


screen = Tk()
screen.title("My Password Manager")
screen.config( padx = 50,pady = 50)

canvas = Canvas(width = 200, height= 200, highlightthickness = 0)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(row = 1, column = 1)


website_label = Label(text="Website",font= ("Courier", 15))
website_label.grid(row = 2, column = 0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row = 2, column = 1, columnspan = 2)

email_label = Label(text="Email/Username",font= ("Courier", 15))
email_label.grid(row = 3, column = 0)

email_entry = Entry(width=35)
email_entry.insert(0,"krishnakhanikar.csed@gmail.com")
email_entry.grid(row = 3, column = 1, columnspan = 2)


pass_label = Label(text="Password",font= ("Courier", 15))
pass_label.grid(row = 4, column = 0)

pass_entry = Entry(width=21)
pass_entry.grid(row = 4, column = 1)

start_button = Button(text="Generate Password", command= pass_gen)
start_button.grid(row = 4, column = 2)

add_button = Button(text="add",width=36, command=file_create)
add_button.grid(row = 5, column = 1,columnspan=2)

screen.mainloop()