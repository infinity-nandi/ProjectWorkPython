from tkinter import *
from CreateButton import create_button

text = ""
def update_text(x):
    global text
    text += str(x)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, text)
def eval_numbers():
    global text
    try:
        text = str(eval(text))
        text_box.delete(1.0, "end")
        text_box.insert(1.0, text)
    except:
        clear_text_box()
        text_box.insert(1.0, "Error")

def clear_text_box():
    global text
    text = ""
    text_box.delete(1.0, "end")

window = Tk()
window.title("Számológép")
window.geometry("250x380")
text_box = Text(window, font=("Helvetica", 24))
text_box.place(x=10, y=10, height=40, width=230)

Seven = create_button(window, "7", 10, 60, 50, 50, command=lambda: update_text(7))
Eight = create_button(window, "8", 70, 60, 50, 50, command=lambda: update_text(8))
Nine = create_button(window, "9", 130, 60, 50, 50, command=lambda: update_text(9))
Four = create_button(window, "4", 10, 120, 50, 50, command=lambda: update_text(4))
Five = create_button(window, "5", 70, 120, 50, 50, command=lambda: update_text(5))
Six = create_button(window, "6", 130, 120, 50, 50, command=lambda: update_text(6))
One = create_button(window, "1", 10, 180, 50, 50, command=lambda: update_text(1))
Two = create_button(window, "2", 70, 180, 50, 50, command=lambda: update_text(2))
Three = create_button(window, "3", 130, 180, 50, 50, command=lambda: update_text(3))
Zero = create_button(window, "0", 70, 240, 50, 50, command=lambda: update_text(0))
OpenBracket = create_button(window, "(", 10, 240, 50, 50, command=lambda: update_text("("))
CloseBracket = create_button(window, ")", 130, 240, 50, 50, command=lambda: update_text(")"))
Add = create_button(window, "+", 190, 60, 50, 50, command=lambda: update_text("+"))
Minus = create_button(window, "-", 190, 120, 50, 50, command=lambda: update_text("-"))
Division = create_button(window, "/", 190, 180, 50, 50, command=lambda: update_text("/"))
Multiplication = create_button(window, "*", 190, 240, 50, 50, command=lambda: update_text("*"))
Equal = create_button(window, "=", 190, 300, 50, 50,bg="deepskyblue",command=eval_numbers)
C = create_button(window, "C", 130, 300, 50, 50,command=clear_text_box)
Save = create_button(window, "Eredmény mentése", 10, 300, 50, 110, font=("Helvetica", 8))

window.mainloop()