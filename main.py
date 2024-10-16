from tkinter import*
screen=Tk()
import random
from time import strftime


screen.geometry("600x150")
screen.title("clock⏰")
screen.config(bg="pale turquoise")
def time():
    text=strftime("%H:%M:%S:%p")
    clock.config (text=text)
    clock.after(1000,time)
clock=Label(screen,text="",bg="pale turquoise",fg="DeepPink",font=("Lucida Handwriting",45,"bold"))


clock.pack(anchor="center",pady=30)
time()
screen.mainloop()