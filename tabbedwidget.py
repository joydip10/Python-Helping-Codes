import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('Practise')

nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text="Page1")
nb.add(page2,text="Page2")

label1=ttk.Label(page1,text="Name:")
label1.grid(row=0,column=0)

entry1=ttk.Entry(page1,width=16)
entry1.grid(row=0,column=1)

nb.pack(expand=True,fill="both")

win.mainloop()