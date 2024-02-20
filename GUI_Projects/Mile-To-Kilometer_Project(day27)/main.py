from tkinter import *


def calculate():
    miles = float(entry.get())
    km = round(1.6 * miles, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile To Kilometer")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)

entry = Entry(width=10)
entry.get()
entry.grid(column=1,row=0)
entry.config()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

button = Button(text="Calculate",command=calculate)
button.grid(column=1, row=2)

window.mainloop()
