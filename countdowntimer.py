from datetime import datetime, date
import tkinter as tk
from tkinter import ttk

def countDown():
    root = tk.Tk()
    present = datetime.now()
    last_working_day = date(2025, 9, 15)
    days_remaining = (last_working_day - date(present.year, present.month, present.day)).days
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text = " " + str(days_remaining) + " days left @ \n Indium Software").grid(column=0, row=0)
    ttk.Button(frm, text = "Close", command = root.destroy).grid(column=1, row=0)
    root.mainloop()

if __name__ == '__main__':
    countDown()