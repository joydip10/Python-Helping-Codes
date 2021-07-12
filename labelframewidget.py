import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('Label Frame Widget')
label_frame=ttk.LabelFrame(win,text='Enter your details below: ')
label_frame.grid(row=0,column=0,sticky=tk.W,padx=40)

label={
      'name':tk.StringVar(),
      'age':tk.StringVar(),
      'email':tk.StringVar(),
      'country':tk.StringVar(),
      'phone_no':tk.StringVar()
}
labels=['name','age','email','country','phone_no']
for i in range(len(label.keys())):
    curr_label=ttk.Label(label_frame,text=labels[i])
    curr_label.grid(row=i,column=0,sticky=tk.W,padx=0,pady=0)
counter=0

for i in label.keys():
    curr_entry=ttk.Entry(label_frame,width=16,textvariable=label.get(i))
    curr_entry.grid(row=counter,column=1,sticky=tk.W,padx=0,pady=0)
    counter=counter+1

def action():
    username=label['name'].get()
    userage=label.get('age').get()
    useremail=label.get('email').get()
    usercountry=label['country'].get()
    userphone=label.get('phone_no').get()
    
    print(f'Name: {username}\nAge: {userage}\nEmail: {useremail}\nCountry: {usercountry}\nPhone: {userphone}\n')
    
submit=ttk.Button(win,text='SUBMIT',command=action)
submit.grid(row=1,columnspan=3)

for child in label_frame.winfo_children():
    child.grid_configure(padx=20,pady=10)
    child.configure(foreground="blue")
win.mainloop()