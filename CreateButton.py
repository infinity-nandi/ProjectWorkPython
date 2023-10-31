from tkinter import Button

class Create_Button:
    @classmethod
    def create_buttons(cls, window, text, x, y, height, width, font=("Helvetica", 20), bg=None, command=None,):
        button = Button(window, text=text, font=font, command=command)
        button.place(x=x, y=y, height=height, width=width)
        if bg:
            button.config(bg=bg)
        return button