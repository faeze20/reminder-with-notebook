from tkinter import *
from datetime import datetime
from playsound import playsound

tk=Tk()
tk.title("reminder")
tk.geometry('500x600')
tk.resizable(width=False, height=False)
title=Label(tk,text="title",bg="green")
title.place(x=70,y=100,width=100)
e_title=Entry(width=30)
e_title.place(x=200, y=100)
hour=Label(tk,text="Hour",bg="green")
hour.place(x=70,y=150,width=100)
e_hour=Entry(width=30)
e_hour.place(x=200, y=150)

display_text=Text(tk,text="",height=10, width=40)
display_text.place(x=250, y=300)

def reminder():
    
    user_time=e_hour.get()
    user_time=datetime.strptime(user_time,"%H:%M:%S").time()
    now_time=datetime.now().time().strftime("%H:%M:%S")
    if now_time==user_time:
         playsound("Mobile Ringtone - Number 2 (320).mp3")
         display_text.delete("1.0", END)
        display_text.insert(END, e_title.get() + ":" + e_hour.get())








reminder=Button(tk,text="reminder",command=reminder,bg="red")
reminder.place(x=250,y=200)



















tk.mainloop()