from tkinter import *
from CreateButton import Create_Button
from datetime import datetime
import math

class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Számológép")
        self.window.geometry("310x380")
        self.window.resizable(False, False)

        self.text = ""
        self.text_box = Text(self.window, font=("Helvetica", 24))
        self.text_box.place(x=10, y=10, height=40, width=290)

        Create_Button.create_buttons(self.window, "7", 10, 60, 50, 50, command=lambda: self.update_text(7))
        Create_Button.create_buttons(self.window, "8", 70, 60, 50, 50, command=lambda: self.update_text(8))
        Create_Button.create_buttons(self.window, "9", 130, 60, 50, 50, command=lambda: self.update_text(9))
        Create_Button.create_buttons(self.window, "4", 10, 120, 50, 50, command=lambda: self.update_text(4))
        Create_Button.create_buttons(self.window, "5", 70, 120, 50, 50, command=lambda: self.update_text(5))
        Create_Button.create_buttons(self.window, "6", 130, 120, 50, 50, command=lambda: self.update_text(6))
        Create_Button.create_buttons(self.window, "1", 10, 180, 50, 50, command=lambda: self.update_text(1))
        Create_Button.create_buttons(self.window, "2", 70, 180, 50, 50, command=lambda: self.update_text(2))
        Create_Button.create_buttons(self.window, "3", 130, 180, 50, 50, command=lambda: self.update_text(3))
        Create_Button.create_buttons(self.window, "0", 70, 240, 50, 50, command=lambda: self.update_text(0))
        Create_Button.create_buttons(self.window, "(", 10, 240, 50, 50, command=lambda: self.update_text("("))
        Create_Button.create_buttons(self.window, ")", 130, 240, 50, 50, command=lambda: self.update_text(")"))
        Create_Button.create_buttons(self.window, "+", 190, 60, 50, 50, command=lambda: self.update_text("+"))
        Create_Button.create_buttons(self.window, "-", 190, 120, 50, 50, command=lambda: self.update_text("-"))
        Create_Button.create_buttons(self.window, "/", 190, 180, 50, 50, command=lambda: self.update_text("/"))
        Create_Button.create_buttons(self.window, "*", 190, 240, 50, 50, command=lambda: self.update_text("*"))
        Create_Button.create_buttons(self.window, "√", 250, 60, 110, 50, command=self.square_root)
        Create_Button.create_buttons(self.window, "π", 250, 180, 50, 50, command=lambda: self.update_text(round(math.pi, 2)))
        Create_Button.create_buttons(self.window, "²", 250, 240, 50, 50, command=self.square)
        Create_Button.create_buttons(self.window, "=", 190, 300, 50, 110, bg="deepskyblue", command=self.eval_numbers)
        Create_Button.create_buttons(self.window, "C", 130, 300, 50, 50, command=self.clear_text_box)
        Create_Button.create_buttons(self.window, "Eredmény mentése", 10, 300, 50, 110, font=("Helvetica", 8), command=self.save_result)



    #text változóban tárolt szöveg újraíródik a text_box-ban, amikor meghívjuk
    def update_text(self, x):
        self.text += str(x)
        self.text_box.delete(1.0, "end") #törli a text_box-ban lévő szöveget
        self.text_box.insert(1.0, self.text) #beilleszti a frissített text tartalmat a szövegdoboz elejére

    def eval_numbers(self):
        try:
            self.text = str(eval(self.text)) #text változó értékének kiértékelése az eval() függvény segítségével.
            #text_box.delete(1.0, "end")
            self.text_box.insert(2.0, "=" + self.text)
            return self.text
        except:
            self.clear_text_box()
            self.text_box.insert(1.0, "Error")
            return None

    def clear_text_box(self):
        self.text = ""
        self.text_box.delete(1.0, "end")

    def save_result(self):
        calculation = self.text_box.get(1.0, "end-1c")  #A text_box tartalmának megszerzése
        if calculation is not None:
            title = f"\nResult of the calculation ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):\n"
            with open("result.txt", "a") as file:
                file.write(title)
                file.write(calculation)
                self.text_box.delete(1.0, "end")
                self.text_box.insert(1.0, "Result saved!")

    def square_root(self):
        global text
        try:
            root = math.sqrt(float(self.text))
            #self.text_box.delete(1.0, "end")
            self.text = str(root)
            self.text_box.insert(2.0, "=" + self.text)
            return self.text
        except:
            self.clear_text_box()
            self.text_box.insert(1.0, "Error")
            return None

    def square(self):
        global text
        squared = math.pow(float(self.text), 2)
        #self.text_box.delete(1.0, "end")
        self.text = str(squared)
        self.text_box.insert(2.0, "=" + self.text)
        return self.text

if __name__ == "__main__":
    window = Tk()
    app = CalculatorApp(window)
    window.mainloop()
