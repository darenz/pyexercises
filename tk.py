import tkinter
from tkinter.constants import *

tk = tkinter.Tk()
tk.geometry("500x300+500+200")

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X,expand=1)


button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)

#messagebox = tkinter.messagebox()
listbox = tkinter.Listbox(tk)
l = ['1','2','3']
for each in l:
    listbox.insert(0,each)
listbox.pack()

entry = tkinter.Entry(frame)
entry.pack()

button2 = tkinter.Button(frame,text='hello')
button2.pack()

tk.mainloop()
