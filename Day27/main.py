import tkinter
from tkinter import Entry, END

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(250,200)
window.config(padx=50, pady=50)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label = tkinter.Label(text="Miles")
label.grid(column=2, row=0)

label = tkinter.Label(text="is equal to")
label.grid(column=0, row=1)

label = tkinter.Label(text="Km")
label.grid(column=2, row=1)

def action():
    miles = entry.get()
    km = round(float(miles) * 1.609344,2)
    label.config(text=km)

label = tkinter.Label(text="0")
label.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=action)
button.grid(column=1, row=2)



window.mainloop()