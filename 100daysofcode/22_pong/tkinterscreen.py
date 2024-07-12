import tkinter as tk

def print_mouse_position(event):
    x, y = event.x_root, event.y_root
    position_label.config(text=f"Mouse position: ({x}, {y})")

def close_window(event):
    root.destroy()

root = tk.Tk()
root.title("Mouse Position Tracker")

# Skapa en etikett för att visa muspekarens position
position_label = tk.Label(root, text="Mouse position: (0, 0)", font=("Helvetica", 16))
position_label.pack(pady=20)

# Binda musrörelser till funktionen
root.bind('<Motion>', print_mouse_position)

# Binda tangenttryckning till att stänga fönstret
root.bind('<Key>', close_window)

# Starta huvudloopen
root.mainloop()
