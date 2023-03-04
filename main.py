from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letter + password_number + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #     password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please make sure that you haven't left any field empty! ")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"These are the details you have entered: Website:{website}\n "
        #                                        f"Email:{email}\nPassword:"f"{password}\nIs this ok to save?")
        try:
            with open("data.json", 'r') as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                # data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json",'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="/Users/mr_verma/Downloads/password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_input = Entry(width=39)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=39)
email_input.insert(0, "itihask56gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=22)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
