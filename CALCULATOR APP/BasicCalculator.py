import tkinter as tk
calc = ""

self = tk.Tk()
self.geometry("361x415")
self.resizable(0, 0)
self.title("Made By Shammo Siddik")
text_input = tk.Text(self, height=3, width=16, font=("Arial", 28))
text_input.grid(columnspan=5)

def basic_calculator(symbol):
    global calc
    calc += str(symbol)
    text_input.delete(1.0, "end")
    text_input.insert(1.0, calc)

def evaluate():
    global calc
    try:
        calculation = str(eval(calc))
        calc = ""
        text_input.delete(1.0, "end")
        text_input.insert(1.0, calculation)
    except:
        clear()
        text_input.insert(1.0, "Error")      
           

def clear():
    global calc
    calc = ""
    text_input.delete(1.0, "end")



button_clear = tk.Button(self, text="C", command=clear, width=5, font=("Arial", 20))
button_clear.grid(row=2, column=1)
button_bracket_open = tk.Button(self, text="(", command=lambda: basic_calculator("("), width=5, font=("Arial", 20))
button_bracket_open.grid(row=2, column=2)
button_bracket_close = tk.Button(self, text=")", command=lambda: basic_calculator(")"), width=5, font=("Arial", 20))
button_bracket_close.grid(row=2, column=3)
button_divide = tk.Button(self, text="/", command=lambda: basic_calculator("/"), width=5, font=("Arial", 20))
button_divide.grid(row=2, column=4) 

button_seven = tk.Button(self, text="7", command=lambda: basic_calculator(7), width=5, font=("Arial", 20))
button_seven.grid(row=3, column=1)
button_eight = tk.Button(self, text="8", command=lambda: basic_calculator(8), width=5, font=("Arial", 20))
button_eight.grid(row=3, column=2)
button_nine = tk.Button(self, text="9", command=lambda: basic_calculator(9), width=5, font=("Arial", 20))
button_nine.grid(row=3, column=3)
button_multiply = tk.Button(self, text="*", command=lambda: basic_calculator("*"), width=5, font=("Arial", 20))
button_multiply.grid(row=3, column=4)

button_four = tk.Button(self, text="4", command=lambda: basic_calculator(4), width=5, font=("Arial", 20))
button_four.grid(row=4, column=1)
button_five = tk.Button(self, text="5", command=lambda: basic_calculator(5), width=5, font=("Arial", 20))
button_five.grid(row=4, column=2)
button_six = tk.Button(self, text="6", command=lambda: basic_calculator(6), width=5, font=("Arial", 20))
button_six.grid(row=4, column=3)
button_subtract = tk.Button(self, text="-", command=lambda: basic_calculator("-"), width=5, font=("Arial", 20))
button_subtract.grid(row=4, column=4)

button_one = tk.Button(self, text="1", command=lambda: basic_calculator(1), width=5, font=("Arial", 20))
button_one.grid(row=5, column=1)
button_two = tk.Button(self, text="2", command=lambda: basic_calculator(2), width=5, font=("Arial", 20))
button_two.grid(row=5, column=2)
button_three = tk.Button(self, text="3", command=lambda: basic_calculator(3), width=5, font=("Arial", 20))
button_three.grid(row=5, column=3)
button_add = tk.Button(self, text="+", command=lambda: basic_calculator("+"), width=5, font=("Arial", 20))
button_add.grid(row=5, column=4)

button_dot = tk.Button(self, text=".", command=lambda: basic_calculator("."), width=5, font=("Arial", 20))
button_dot.grid(row=6, column=1)
button_zero = tk.Button(self, text="0", command=lambda: basic_calculator(0), width=5, font=("Arial", 20))
button_zero.grid(row=6, column=2)
button_equal = tk.Button(self, text="=", command=evaluate, width=10, font=("Arial", 20))
button_equal.grid(row=6, column=3, columnspan=2)

self.mainloop()