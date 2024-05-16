#Уровень С третье задание
# Поле для ввода чисел сверху окна, оно просто незаметное

import tkinter as tk
def calculate():
    numbers = entry.get().split('+')
    result = sum(map(int, numbers))
    result_label.config(text=f"Результат: {result}")


root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="=", width=10, command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=10)

root.mainloop()
