from tkinter import Button

def create_button(window, text, x, y, height, width, font=("Helvetica", 20), bg=None, command=None):
    button = Button(window, text=text, font=font, command=command)
    button.place(x=x, y=y, height=height, width=width)
    if bg:
        button.config(bg=bg)
    return button