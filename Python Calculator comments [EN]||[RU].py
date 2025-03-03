[EN]
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.configure(bg='lightblue')

# Create the entry widget to display the input and result
entry = tk.Entry(window, width=20, font=('Arial', 24), justify="right", bd=10, insertwidth=2, bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize variables to store the current value and operation
current_value = 0
current_operation = None

# Define the callback function for button clicks
def on_click(value):
    global current_value, current_operation
    if value.isdigit():
        # If the button is a digit, append it to the entry widget
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)
    elif value in ['+', '-', '*', '/']:
        # If the button is an operation, store the current value and operation
        current_value = float(entry.get())
        current_operation = value
        entry.delete(0, tk.END)
    elif value == '=':
        # If the button is '=', perform the calculation
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
        # If the button is 'C', clear the entry and reset variables
        entry.delete(0, tk.END)
        current_value = 0
        current_operation = None

# Create the digit buttons and place them in the grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, font=('Arial', 18), bg='white', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Create the operation buttons and place them in the grid
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('=', 4, 2), ('C', 4, 0)
]

for (text, row, col) in operations:
    tk.Button(window, text=text, font=('Arial', 18), bg='orange', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Run the main event loop
window.mainloop()

[RU]
import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x500")
window.configure(bg='lightblue')

# Создаем виджет ввода для отображения ввода и результата
entry = tk.Entry(window, width=20, font=('Arial', 24), justify="right", bd=10, insertwidth=2, bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Инициализируем переменные для хранения текущего значения и операции
current_value = 0
current_operation = None

# Определяем функцию обратного вызова для нажатий кнопок
def on_click(value):
    global current_value, current_operation
    if value.isdigit():
        # Если кнопка является цифрой, добавляем ее к виджету ввода
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)
    elif value in ['+', '-', '*', '/']:
        # Если кнопка является операцией, сохраняем текущее значение и операцию
        current_value = float(entry.get())
        current_operation = value
        entry.delete(0, tk.END)
    elif value == '=':
        # Если кнопка '=', выполняем расчет
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
        # Если кнопка 'C', очищаем виджет ввода и сбрасываем переменные
        entry.delete(0, tk.END)
        current_value = 0
        current_operation = None

# Создаем кнопки с цифрами и размещаем их в сетке
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, font=('Arial', 18), bg='white', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Создаем кнопки операций и размещаем их в сетке
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('=', 4, 2), ('C', 4, 0)
]

for (text, row, col) in operations:
    tk.Button(window, text=text, font=('Arial', 18), bg='orange', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Запускаем главный цикл событий
window.mainloop()
