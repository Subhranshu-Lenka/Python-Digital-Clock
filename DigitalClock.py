from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Digital Clock")

clock = Label(root, font=("Arial", 50), bg="grey", fg="white")
clock.pack()


def get_time():
    timer = time.strftime("%I:%M:%S %p")
    clock.config(text=timer)
    clock.after(100, get_time)


# print(type(clock))
get_time()


root.mainloop()
