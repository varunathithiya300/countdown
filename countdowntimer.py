from datetime import datetime, date
import tkinter as tk
from tkinter import messagebox, ttk

def countDown(year: int, month: int, day: int) -> int:
    current_date = date(year, month, day)
    last_working_day = date(2025, 9, 15)
    delta_in_days = last_working_day - current_date
    return delta_in_days.days

def showPopup():
    root = tk.Tk()
    present = datetime.now()
    days_remaining = countDown(present.year, present.month, present.day)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text = " " + str(days_remaining) + " days left @ \n Indium Software").grid(column=0, row=0)
    ttk.Button(frm, text = "Close", command = root.destroy).grid(column=1, row=0)
    root.mainloop()

if __name__ == '__main__':
    showPopup()