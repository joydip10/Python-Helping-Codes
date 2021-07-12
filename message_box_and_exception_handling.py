import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('Message Box and Exception Handling')

labelframe=ttk.LabelFrame(win,text='Fill the following fields: ')
labelframe.grid(row=0,column=0,padx=30)

label1=ttk.Label(labelframe,text='Enter your name please: ')
label1.grid(row=0,column=0,sticky=tk.W)

label2=ttk.Label(labelframe,text='Enter your age please: ')
label2.grid(row=0,column=1,sticky=tk.W)

entry1_var=tk.StringVar()
entry1=ttk.Entry(labelframe,width=22,textvariable=entry1_var)
entry1.grid(row=1,column=0,sticky=tk.W)

entry2_var=tk.StringVar()
entry2=ttk.Entry(labelframe,width=22,textvariable=entry2_var)
entry2.grid(row=1,column=1,sticky=tk.W)


for child in labelframe.winfo_children():
    child.grid_configure(padx=2,pady=0)
    child.configure(foreground='blue')
def action():
    username=entry1_var.get()
    userage=entry2_var.get()
    try:
        age=int(userage)
    except:
        m_box.showerror('Error','ValueError has been done')
    else:
        print(f'Age :{userage}')

           
        
        
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    
    
submit=ttk.Button(win,command=action,text='SUBMIT')
submit.grid(row=1,columnspan=3)

win.mainloop()