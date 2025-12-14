import tkinter as tk
from tkinter import messagebox
from bmi_logic import calculate_bmi, bmi_category
from database import connect_db, insert_data, fetch_user_data
from visualization import show_bmi_trend

conn = connect_db()

def calculate():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")
        insert_data(conn, name, weight, height, bmi)

    except ValueError:
        messagebox.showerror("Error", "Enter valid weight & height")


def view_graph():
    name = name_entry.get()
    data = fetch_user_data(conn, name)

    if not data:
        messagebox.showinfo("No Data", "No BMI records found")
        return

    show_bmi_trend(data, name)


root = tk.Tk()
root.title("Advanced BMI Calculator")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Weight (kg)").grid(row=1, column=0)
tk.Label(root, text="Height (m)").grid(row=2, column=0)

name_entry = tk.Entry(root)
weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
weight_entry.grid(row=1, column=1)
height_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate BMI", command=calculate).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="View BMI Trend", command=view_graph).grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
