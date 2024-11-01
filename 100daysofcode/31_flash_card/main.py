from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")

# ---------------------------- Words to read ------------------------------- #
words_completed = []
# Funktion för att byta till engelska ordet efter timer
def show_english_card(current_card):
    canvas.itemconfig(bg_canvas, image=card_back_image)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(word_title, text=data['English'][current_card])

# Funktion för att starta nästa kort och timer
def next_card():
    canvas.itemconfig(bg_canvas, image=card_front_image)
    current_card = random.randint(0, len(data) - 1)
    
    # Kontrollera om kortet redan är slutfört
    if current_card not in words_completed:
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(word_title, text=data['French'][current_card])
        print(data['English'][current_card])  # Visar engelska ordet i terminalen för kontroll
        words_completed.append(current_card)
        
        # Starta timer för att visa engelska efter 3 sekunder
        window.after(3000, lambda: show_english_card(current_card))


# ---------------------------- Store progress ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_canvas = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400, 150, text='Title',font=("Ariel", 40, "italic"))
word_title = canvas.create_text(400, 263, text='Word',font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, padx=50, pady=50, columnspan=2)

#Labels




right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=next_card) 
right_button.grid(row=10, column=1, padx=10, pady=10)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=next_card)
wrong_button.grid(row=10, column=2, padx=10, pady=10)




window.mainloop()

