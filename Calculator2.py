import tkinter as tk

# Function to calculate the result of the expression
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle button presses
def button_press(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the Entry widget
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_press("1"))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_press("2"))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_press("3"))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_press("4"))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_press("5"))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_press("6"))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_press("7"))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_press("8"))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_press("9"))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_press("0"))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_press("+"))
button_minus = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_press("-"))
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=calculate)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=lambda: entry.delete(0, tk.END))

# Put the buttons on the screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_minus.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()