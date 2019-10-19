#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import barlib


win = tk.Tk()
a5 = PhotoImage(file="g1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("ProTerra")
win.geometry("800x400+0+0")
win.resizable(width=True, height=True)
win.configure(bg='black')
def exitProgram():
    if messagebox.askyesno("Print", "Exit?"):
        win.destroy()       
originalPlantImage = tk.PhotoImage(file="exit.png")
image = originalPlantImage.subsample(15, 15)
exitb = tk.Button(win,
        text="Exit",
        image=image,
        font=("Helvetica", 14,'bold'),
        compound="left",
        borderwidth=3,
        width = 60,
        height = 30,              
        bg="lightskyblue",
        fg='black',
        command= exitProgram,
        activebackground="dark gray")
exitb.pack(fill=X,padx=2)
def read_every_second():
    g_value=random.randint(0,100)
    bar1.set_value2(int(g_value))
    g_value=random.randint(0,100)
    bar2.set_value(int(g_value))
    win.after(100, read_every_second)

bar1 = barlib.DrawBar(
    win,
    max_value=100.0,
    min_value=0.0,
    size=300,
    bg_col='black',
    bg_sel =2,
    unit = "Temp. °C")
bar1.pack(side=LEFT)

bar2 = barlib.DrawBar(
    win,
    max_value=100.0,
    min_value=0.0,
    size=200,
    bg_col='black',
    bg_sel =1,
    unit = "Temp. °C")
bar2.pack(side=LEFT)

read_every_second()
mainloop()
