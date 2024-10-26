from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=500, height=300)


#Label
km_text = Label(text="0", font=("Arial", 24 ,"bold"))
km_text.grid(row=0, column=3)

label_text = Label(text="KM", font=("Arial", 24 ,"bold"))
label_text.grid(row=0, column=4)

#Label
label_text = Label(text="Miles", font=("Arial", 24 ,"bold"))
label_text.grid(row=1, column=4)


def button_clicked():
    km = round(float(entry_field.get()) * 1.609344 ,2)
    km_text["text"] = km


#Button
button = Button(text="Convert", command=button_clicked)
button.grid(row=1, column=2)


#Entry
entry_field = Entry()
entry_field.grid(row=1, column=3)









window.mainloop()