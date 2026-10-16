import tkinter as tk
import math

# Function to evaluate expressions safely
def evaluate_expression(expr):
    try:
        expr = expr.replace("^", "**")

        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")

        result = eval(expr, {"math": math, "__builtins__": {}})
        return result

    except Exception as e:
        return f"Error: {e}"

# Function to handle button clicks
def on_button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate_result():
    expr = entry.get()
    result = evaluate_expression(expr)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

# Entry widget for input
entry = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

# Button layout
buttons = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "^"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "(", ")", "ln"],
    ["sin", "cos", "tan", "+", "="],
    ["C"]
]

# Create buttons dynamically
for r, row in enumerate(buttons, start=1):
    for c, symbol in enumerate(row):
        if symbol == "=":
            btn = tk.Button(root, text=symbol, font=("Arial", 14), command=calculate_result)
        elif symbol == "C":
            btn = tk.Button(root, text=symbol, font=("Arial", 14), command=clear_entry)
        else:
            btn = tk.Button(root, text=symbol, font=("Arial", 14), command=lambda s=symbol: on_button_click(s))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Make grid cells expand
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
