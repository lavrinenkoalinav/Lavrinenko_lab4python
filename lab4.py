import tkinter as tk
from tkinter import messagebox

def on_button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry_var.get())  # Виконуємо обчислення
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Помилка", "Некоректний вираз")
    elif symbol == "C":
        entry_var.set("")  # Очищення поля вводу
    else:
        entry_var.set(entry_var.get() + str(symbol))

# Головне вікно
root = tk.Tk()
root.title("Калькулятор")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.GROOVE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Розташування кнопок
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

for r, row in enumerate(buttons, 1):
    for c, symbol in enumerate(row):
        btn = tk.Button(root, text=symbol, font=("Arial", 20), width=5, height=2, command=lambda s=symbol: on_button_click(s))
        btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
