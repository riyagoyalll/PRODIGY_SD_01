import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result.set(f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K")
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result.set(f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K")
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result.set(f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F")
        else:
            result.set("Select a valid unit!")
    except ValueError:
        result.set("Enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")

title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
unit_menu.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12), bg="blue", fg="white")
convert_btn.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12), fg="green")
result_label.pack(pady=10)

root.mainloop()