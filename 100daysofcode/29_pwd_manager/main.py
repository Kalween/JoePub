from tkinter import *
import string
import random
import pandas as pd
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Lista med alla små bokstäver, stora bokstäver, siffror och specialtecken
def pwd_gen():
    alfabet_små = list(string.ascii_lowercase)
    alfabet_stora = list(string.ascii_uppercase)
    siffror = list(string.digits)
    specialtecken = list(string.punctuation)

    lösenord = []
    # Kombinera alla i en lista
    for _ in range(int(spinbox1.get())):
        lösenord.append(random.choice([random.choice(alfabet_små), random.choice(alfabet_stora)]))

        
    for _ in range(int(spinbox2.get())):    
        lösenord.append(random.choice(siffror))

    for _ in range(int(spinbox3.get())):    
        lösenord.append(random.choice(specialtecken))
    random.shuffle(lösenord)
    generate_entry.delete(0, "end")
    generate_entry.insert(END,"".join(lösenord))
    print("".join(lösenord))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pwd():
    
    data_to_export = {
        "site":[site_entry.get()],
        "Username":[username_entry.get()],
        "Password":[generate_entry.get()]
        }
    new_df = pd.DataFrame(data_to_export)
    if os.path.exists("logs.csv"):
        new_df.to_csv("logs.csv", mode="a", index=False, header=False, encoding="utf-8")
    else:
        new_df.to_csv("logs.csv", mode="w", index=False, encoding="utf-8")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pwd Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=224, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 112, image=img)
canvas.grid(row=1, column= 1)

# Labels
username_label = Label(text='Username')
username_label.grid(row=2, column=0)

stored_password_label = Label(text='Password')
stored_password_label.grid(row=2, column=2)

site_label = Label(text='Site')
site_label.grid(row=4, column=0)

generate_label = Label(text='Generate')
generate_label.grid(row=5, column=1)



#Spinboxes
START_VALUE_ALPH = IntVar(value=5)
START_VALUE_NUMB = IntVar(value=5)
START_VALUE_CHAR = IntVar(value=2)

start_value = IntVar(value=5)
spinbox1_label = Label(text='Letters')
spinbox1_label.grid(row=9, column=0)
spinbox1 = Spinbox(from_=0, to=10, width=5,textvariable=START_VALUE_ALPH)
spinbox1.grid(row=8,column=0, pady=40)

spingbox2_label = Label(text='Numbers')
spingbox2_label.grid(row=9, column=1)
spinbox2 = Spinbox(from_=0, to=10, width=5,textvariable=START_VALUE_NUMB)
spinbox2.grid(row=8,column=1, pady=40)

spingbox3_label = Label(text='Special-characters')
spingbox3_label.grid(row=9, column=2)
spinbox3 = Spinbox(from_=0, to=10, width=5,textvariable=START_VALUE_CHAR)
spinbox3.grid(row=8,column=2, pady=40)


# Entry
username_entry = Entry()
username_entry.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=2)

site_entry = Entry()
site_entry.grid(row=5, column=0)
site_entry.focus()

generate_entry = Entry()
generate_entry.grid(row=6, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=pwd_gen)
generate_button.grid(row=7, column=1)

save_button = Button(text="Save Password", command=save_pwd)
save_button.grid(row=6, column=2)




window.mainloop()