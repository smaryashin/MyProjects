import tkinter as tk
from tkinter import ttk


def calculate(first_entry, second_entry, result_entry):
    first = int(first_entry.get())
    second = int(second_entry.get())
    total = first + second
    result_entry.configure(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(total))
    result_entry.configure(state="readonly")


def main():
    root = tk.Tk()
    root.title("Сумма двух чисел")

    ttk.Label(root, text="Первое число:").grid(row=0, column=0, padx=8, pady=6, sticky="w")
    first_entry = ttk.Entry(root, width=20)
    first_entry.grid(row=0, column=1, padx=8, pady=6)

    ttk.Label(root, text="Второе число:").grid(row=1, column=0, padx=8, pady=6, sticky="w")
    second_entry = ttk.Entry(root, width=20)
    second_entry.grid(row=1, column=1, padx=8, pady=6)

    ttk.Label(root, text="Результат:").grid(row=2, column=0, padx=8, pady=6, sticky="w")
    result_entry = ttk.Entry(root, width=20, state="readonly")
    result_entry.grid(row=2, column=1, padx=8, pady=6)

    calculate_button = ttk.Button(
        root,
        text="Calculate",
        command=lambda: calculate(first_entry, second_entry, result_entry),
    )
    calculate_button.grid(row=3, column=0, columnspan=2, padx=8, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
