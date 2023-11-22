from tkinter import Button

class Create_Button:
    @classmethod #nem szükséges az osztály példányosítása a használathoz
    def create_buttons(cls, window, text, x, y, height=50, width=50, font=("Helvetica", 20), bg=None, command=None,):
        button = Button(window, text=text, font=font, command=command)
        button.place(x=x, y=y, height=height, width=width)
        if bg:
            button.config(bg=bg)
        return button