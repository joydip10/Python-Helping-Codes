#starter code
import tkinter as tk
from tkinter import ttk
from csv import reader, writer,DictReader,DictWriter
import os
#from tkinter import tkinter*

win=tk.Tk()
win.title('GUI')

#widgets-->labels, buttons, radiobuttons-> tk. ttk

#create labels
name_label=ttk.Label(win,text='Enter Your Name: ')
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='Enter Email: ')
email_label.grid(row=2,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter Your Age: ')
age_label.grid(row=3,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Specify your gender: ")
gender_label.grid(row=4,column=0,sticky=tk.W)

#.pack() .grid() .place()


#Create Entry box
name_var=tk.StringVar()
name_entry=ttk.Entry(win,width=16,textvariable=name_var)
name_entry.grid(row=0,column=1,sticky=tk.W)
name_entry.focus()

email_var=tk.StringVar()
email_entry=ttk.Entry(win,width=16,textvariable=email_var)
email_entry.grid(row=2,column=1,sticky=tk.W)

age_var=tk.StringVar()
age_entry=ttk.Entry(win,width=16,textvariable=age_var)
age_entry.grid(row=3,column=1,sticky=tk.W)


'''
#create Button
def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    
    print(f"{username} is {userage} years old and Email Id of {username} is {useremail}\n")
    

submit_button=ttk.Button(win,text="SUBMIT",command=action)
submit_button.grid(row=4,column=0,sticky=tk.W)
'''

#combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('male','female','others')
gender_combobox.grid(row=4,column=1)
gender_combobox.current(0)


#radiobutton
usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtn1.grid(row=5,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=5,column=1)


#CheckButton

chkbtn_var=tk.IntVar()
chkbtn=ttk.Checkbutton(win,text='Check it if you want to subscribe',variable=chkbtn_var)
chkbtn.grid(row=6,column=0,columnspan=3)


#Submit Button

def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    usergender=gender_var.get()
    userprofession=profession_var.get()
    usersubscription=chkbox_subscribed_var.get()
    
    if username and userage and useremail and usergender and userprofession:
        print(f'Name of the user: {username}\nAge of the user: {userage}\nEmail ID of the user: {useremail}\nProfession of the user: {userprofession}\n')
    if usersubscription==0 and username and userage and useremail and usergender and userprofession:
        print('Subscription done: No\n')
    if usersubscription==1 and username and userage and useremail and usergender and userprofession:
        print('Subscription done: Yes\n')
    
    if username and userage and useremail:
        with open('Gui.txt','a') as wf:
            wf.write(f"{username},{userage},{useremail}\n")
    
    with open('Gui.txt','r') as rf:
        print(rf.read())
    
    
    if username and userage and useremail and usergender:
        with open("GUI.csv",'a',newline='') as wf:
            csv_reader=DictWriter(wf,fieldnames=['Name','Age','Email','Gender'])
            if os.stat('GUI.csv').st_size==0:    #This line prevents the fielnames from getting copied every times
                csv_reader.writeheader()
            csv_reader.writerow({
                    'Name':username,
                    'Age':userage,
                    'Email':useremail,
                    'Gender':usergender
                    })
    
    with open('GUI.csv','r') as rf:
        csv_reader=DictReader(rf,delimiter=',')
        for i in csv_reader:
            print(i)
            
    #deleting the entry text box after pressing the submit button
    name_entry.delete(0,tk.END) 
    age_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    
    #Changing foreground the labels using configure
    name_label.config(foreground='Blue')
    age_label.config(foreground='Blue')
    email_label.config(foreground='Blue')   
    #we can't change the ttk buttons using config
               

submit_button=ttk.Button(win,text="SUBMIT",command=action)
submit_button.grid(row=7,column=0,sticky=tk.W)


















win.mainloop()



