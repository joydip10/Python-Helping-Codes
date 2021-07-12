import tkinter as tk
import requests
from tkinter import font
HEIGHT=500
WIDTH=600

root=tk.Tk()
root.title('WEATHERLY')
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
#153ce5bf1df68ef5eba169796ff27808

#background_image=tk.PhotoImage(file='nature.PNG')
#background_label=tk.Label(root,image=background_image)
#background_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root,bg='#33FFEC',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')


entry=tk.Entry(frame,bg='white',font=('Courier',18))
entry.place(relwidth=0.65,relheight=1)
entry.focus()

def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
    
        final_str=f'City: {str(name)}\nConditions: {str(desc)}\nTemperature: {str(temp)}'
    
    except:
        final_str='There is a problem retrieving that information'
    
    return final_str    
def get_weather(city):
    weather_key='153ce5bf1df68ef5eba169796ff27808'
    url='https://api.openweathermap.org/data/2.5/weather'  
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params=params)
    weather=response.json()
    
    label['text']=format_response(weather)
    
    
button=tk.Button(frame,text='Get Weather',bg='gray',font=('Courier',12),command=lambda: get_weather(entry.get()))
button.place(relx=0.65,rely=0,relwidth=0.35,relheight=1)

lower_frame=tk.Frame(root,bg='#33FFEC',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,bg='white',font=('Courier',18),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)



root.mainloop()