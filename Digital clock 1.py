from tkinter import * 
import tkinter as t
import datetime as d
rt=t.Tk()  #main window
rt.title("DIGITAL CLOCK")
rt.geometry("500x500")  #SCREENSIZE
rt.configure(bg="black")
def now():
    tym=(d.datetime.now())
    a=tym.strftime("%I:%M:%S %p")  #I [12 hr], M [60 minute], S [60 seconds], p [AM/PM]
    lbl=Label(rt, text=a,bg="grey",fg="black")  #TO DISPLAY OUTPUT
    lbl.pack()
    
btn=t.Button(rt,text='Time',width=20,command=now) #BTN SYNTAX
btn.pack()
rt.mainloop()
