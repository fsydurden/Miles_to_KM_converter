import tkinter
from tkinter import Button,Entry

window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width=500,height=300)

def calculate():
    miles = input.get()
    km = int(miles) * 1.60934
    label2 = tkinter.Label(text=km)
    label2.grid(column=1, row=2)

input = Entry()
input.grid(column=1,row=0)

label = tkinter.Label(text="Is equal to")
label.grid(column=0,row=2)



button = Button(text="calculate", command=calculate)
button.grid(column=1,row=3)

label3 = tkinter.Label(text="KM")
label3.grid(column=2,row=2)


window.mainloop()
