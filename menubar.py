import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('Menu')

'''
#Simple Menu
menu=tk.Menu(win)

def action():
    pass

menu.add_command(label='File',command=action)
menu.add_command(label='Edit',command=action)
menu.add_command(label='Tools',command=action)
menu.add_command(label='Tabs',command=action)



win.config(menu=menu)
'''

#Tabbed Menu
menu=tk.Menu(win)
File_menu=tk.Menu(menu,tearoff=0)
Edit_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=File_menu)
menu.add_cascade(label='Edit',menu=Edit_menu)

def action():
    pass

File_menu.add_command(label='New fIle',command=action)
File_menu.add_command(label='Open',command=action)
File_menu.add_separator()
File_menu.add_command(label='Save as',command=action)
File_menu.add_command(label='Save',command=action)
File_menu.add_separator()

Edit_menu.add_command(label='Find',command=action)
Edit_menu.add_command(label='Delete',command=action)
Edit_menu.add_separator()
Edit_menu.add_command(label='Undo',command=action)
Edit_menu.add_command(label='Redo',command=action)
Edit_menu.add_separator()

win.config(menu=menu)



win.mainloop()