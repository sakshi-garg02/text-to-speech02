import tkinter #for gui 
from tkinter import *

import pyttsx3

   
top = Tk()  #creating the application main window.

top.title("TEXT to SPEAK")
top.geometry("800x400")

def speak():
    e=pyttsx3.init()
    voice=e.getProperty('voices')
    
    
    
#condition===
    if var.get()==1:
        e.setProperty('voice',voice[0].id)
        #e.say(Text.get())
        e.say(Text.get().partition("#")[0].rstrip())
        e.runAndWait()
        
    else:
        e.setProperty('voice',voice[1].id)
        e.say(Text.get().partition("#")[0].rstrip())
        e.runAndWait()
        
def clear():
    Text.delete(0,END)

def save():
    e=pyttsx3.init()
    e.save_to_file("voice",'test.mp3')
    

    
Label(top, text = 'Enter your text here :', font =('Verdana', 30)).pack(side = TOP, pady= 40)
Text=Entry(top,font=30)
Text.pack(pady=12)

var = IntVar()
R1 = Radiobutton(top, text="MALE", variable=var, value=1)
R1.pack()

R2 = Radiobutton(top, text="FEMALE", variable=var, value=2)
R2.pack()



b1 = Button(top,text = "Speak",command=speak,bg="orange",height=2,width=8,activebackground="#fff5cc",font =('Verdana', 13))
b1.pack(pady=10)
b2 = Button(top,text = "Clear",command=clear,bg="red",height=2,width=8,activebackground="#ffad99",font =('Verdana', 13))
b2.pack(pady=10)


top.mainloop()  #Entering the event main loop
