from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")

# ---------------------------- Words to read ------------------------------- #
words_completed = []
def word_game():
    flashcard_timer = 3
    random_word = random.randint(1, len(data))
    
    if random_word not in words_completed:
        print(data['French'][random_word])
        if flashcard_timer > 0:
            window.after(1000, flashcard_timer -1)
        print(data['English'][random_word])
        words_completed.append(random_word)
    return data['French'][random_word]



# ---------------------------- Store score ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400,263,image=card_front_image)
canvas.create_text(400, 150, text='Title',font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text=word_game(),font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, padx=50, pady=50, columnspan=2)

#Labels




right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=word_game()) 
right_button.grid(row=10, column=1, padx=10, pady=10)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
wrong_button.grid(row=10, column=2, padx=10, pady=10)




window.mainloop()

