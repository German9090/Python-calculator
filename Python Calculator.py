import tkinter as tk

window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x500")
window.configure(bg='lightblue')

entry = tk.Entry(window, width=20, font=('Arial', 24), justify="right", bd=10, insertwidth=2, bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

current_value = 0
current_operation = None

def on_click(value):
    global current_value, current_operation
    if value.isdigit():
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)
    elif value in ['+', '-', '*', '/']:
        current_value = float(entry.get())
        current_operation = value
        entry.delete(0, tk.END)
    elif value == '=':
        second_value = float(entry.get())
        entry.delete(0, tk.END)
        result = 0
        if current_operation == '+':
            result = current_value + second_value
        elif current_operation == '-':
            result = current_value - second_value
        elif current_operation == '*':
            result = current_value * second_value
        elif current_operation == '/':
            result = current_value / second_value
        if result.is_integer():
            result = int(result)
        entry.insert(0, result)
    elif value == 'C':
        entry.delete(0, tk.END)
        current_value = 0
        current_operation = None

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, font=('Arial', 18), bg='white', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('=', 4, 2), ('C', 4, 0)
]

for (text, row, col) in operations:
    tk.Button(window, text=text, font=('Arial', 18), bg='orange', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

window.mainloop()