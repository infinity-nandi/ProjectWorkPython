from tkinter import *
from CreateButton import create_button

window = Tk()
window.title("Számológép")
window.geometry("250x380")
text_box = Text(window, font=("Helvetica", 24))
text_box.place(x=10, y=10, height=40, width=230)

Seven = create_button(window, "7", 10, 60, 50, 50)
Eight = create_button(window, "8", 70, 60, 50, 50)
Nine = create_button(window, "9", 130, 60, 50, 50)
Four = create_button(window, "4", 10, 120, 50, 50)
Five = create_button(window, "5", 70, 120, 50, 50)
Six = create_button(window, "6", 130, 120, 50, 50)
One = create_button(window, "1", 10, 180, 50, 50)
Two = create_button(window, "2", 70, 180, 50, 50)
Three = create_button(window, "3", 130, 180, 50, 50)
Zero = create_button(window, "0", 10, 240, 50, 170)
Add = create_button(window, "+", 190, 60, 50, 50)
Minus = create_button(window, "-", 190, 120, 50, 50)
Division = create_button(window, "/", 190, 180, 50, 50)
Multiplication = create_button(window, "*", 190, 240, 50, 50)
Equal = create_button(window, "=", 190, 300, 50, 50, bg="deepskyblue")
C = create_button(window, "C", 130, 300, 50, 50)
Save = create_button(window, "Eredmény mentése", 10, 300, 50, 110, font=("Helvetica", 8))

window.mainloop()