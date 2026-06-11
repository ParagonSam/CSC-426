import tkinter as tk
import math

# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        # Replace '^' with '**' for python exponentiation
        # Replace '\' with '//' for floor division
        expr = expression.replace('^', '**').replace('\\', '//')
        total = str(eval(expr))
        equation.set(total)
        expression = total # keep the result for further calculations
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window setup
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("320x400")
root.configure(bg="#333333")

expression = ""
equation = tk.StringVar()

# Display Screen
display = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=4, width=16, borderwidth=0, justify="right")
display.grid(columnspan=4, ipady=15, padx=10, pady=10)

# Button configurations
button_config = {
    'font': ("Arial", 14),
    'fg': "#ffffff",
    'bg': "#555555",
    'activebackground': "#777777",
    'activeforeground': "#ffffff",
    'borderwidth': 0,
    'height': 2,
    'width': 5
}

# Row 1: C, \, ^, %
clear_btn = tk.Button(root, text='C', command=clear, **button_config, bg="#d9534f")
clear_btn.grid(row=1, column=0, padx=5, pady=5)

floor_btn = tk.Button(root, text='\\', command=lambda: press('\\'), **button_config, bg="#f0ad4e")
floor_btn.grid(row=1, column=1, padx=5, pady=5)

pow_btn = tk.Button(root, text='^', command=lambda: press('^'), **button_config, bg="#f0ad4e")
pow_btn.grid(row=1, column=2, padx=5, pady=5)

mod_btn = tk.Button(root, text='%', command=lambda: press('%'), **button_config, bg="#f0ad4e")
mod_btn.grid(row=1, column=3, padx=5, pady=5)

# Row 2: 7, 8, 9, /
b7 = tk.Button(root, text='7', command=lambda: press(7), **button_config)
b7.grid(row=2, column=0, padx=5, pady=5)
b8 = tk.Button(root, text='8', command=lambda: press(8), **button_config)
b8.grid(row=2, column=1, padx=5, pady=5)
b9 = tk.Button(root, text='9', command=lambda: press(9), **button_config)
b9.grid(row=2, column=2, padx=5, pady=5)
div_btn = tk.Button(root, text='/', command=lambda: press('/'), **button_config, bg="#f0ad4e")
div_btn.grid(row=2, column=3, padx=5, pady=5)

# Row 3: 4, 5, 6, *
b4 = tk.Button(root, text='4', command=lambda: press(4), **button_config)
b4.grid(row=3, column=0, padx=5, pady=5)
b5 = tk.Button(root, text='5', command=lambda: press(5), **button_config)
b5.grid(row=3, column=1, padx=5, pady=5)
b6 = tk.Button(root, text='6', command=lambda: press(6), **button_config)
b6.grid(row=3, column=2, padx=5, pady=5)
mul_btn = tk.Button(root, text='*', command=lambda: press('*'), **button_config, bg="#f0ad4e")
mul_btn.grid(row=3, column=3, padx=5, pady=5)

# Row 4: 1, 2, 3, -
b1 = tk.Button(root, text='1', command=lambda: press(1), **button_config)
b1.grid(row=4, column=0, padx=5, pady=5)
b2 = tk.Button(root, text='2', command=lambda: press(2), **button_config)
b2.grid(row=4, column=1, padx=5, pady=5)
b3 = tk.Button(root, text='3', command=lambda: press(3), **button_config)
b3.grid(row=4, column=2, padx=5, pady=5)
sub_btn = tk.Button(root, text='-', command=lambda: press('-'), **button_config, bg="#f0ad4e")
sub_btn.grid(row=4, column=3, padx=5, pady=5)

# Row 5: 0, ., =, +
b0 = tk.Button(root, text='0', command=lambda: press(0), **button_config)
b0.grid(row=5, column=0, padx=5, pady=5)
dot_btn = tk.Button(root, text='.', command=lambda: press('.'), **button_config)
dot_btn.grid(row=5, column=1, padx=5, pady=5)
equal_btn = tk.Button(root, text='=', command=equalpress, **button_config, bg="#5cb85c", width=12)
equal_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5)
add_btn = tk.Button(root, text='+', command=lambda: press('+'), **button_config, bg="#f0ad4e")
add_btn.grid(row=6, column=3, padx=5, pady=5) # Adjust layout placement cleanly

# Repositioning + button to keep grid uniform
add_btn.grid(row=5, column=3, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()