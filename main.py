from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():                #define the time func
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")        #setting the font ,background, foreground
label.pack(anchor='center')
time()                            #call the time func

mainloop()
