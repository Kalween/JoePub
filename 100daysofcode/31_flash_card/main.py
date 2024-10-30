from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Words to read ------------------------------- #


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
canvas.grid(row=1, column=1, padx=50, pady=50, columnspan=2)


right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0) 
right_button.grid(row=10, column=1, padx=10, pady=10)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
wrong_button.grid(row=10, column=2, padx=10, pady=10)




window.mainloop()

