from tkinter import *
THEME_COLOR = "#375362"
BUTTON_TRUE = 'images/true.png'
BUTTON_FALSE = 'images/false.png'

window = Tk()

window.title("Quizz App")
window.config(background=THEME_COLOR)

canvas = Canvas(width=800, height=526)
true_img = PhotoImage(file=BUTTON_TRUE)
false_img = PhotoImage(file=BUTTON_FALSE)

button_true = Button(image=true_img, highlightthickness=0)
button_true.grid(row=10, column=0)

button_false = Button(image=false_img, highlightthickness=0)
button_false.grid(row=10, column=1)




window.mainloop()