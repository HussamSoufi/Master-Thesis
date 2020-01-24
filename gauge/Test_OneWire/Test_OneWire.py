#!/usr/bin/env python3
from tkinter import *
from collections import deque
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import threading
import ThermometerLib
import gaugelib
import sys
import csv
import subprocess
from subprocess import call
import time
import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates
import os


win = tk.Tk()
a5 = PhotoImage(file="g1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("ProTerra")
win.geometry("700x400+0+0")
win.resizable(width=True, height=True)
win.configure(bg='gray10')
def exitProgram():
    #if messagebox.askyesno("Print", "Exit?"):
        thread2.x=1
        win.destroy()       
originalPlantImage = tk.PhotoImage(file="exit.png")
image = originalPlantImage.subsample(15, 15)
def pHgraph():
    call(["python", "gauge\Test_OneWire\pHgraph.py"])
def ORPgraph():
    call(["python3", "ORPgraph.py"])
def Tempgraph():
    call(["python3", "Tempgraph.py"])
def DOgraph():
    call(["python3", "DOgraph.py"])
def ECgraph():
    call(["python3", "ECgraph.py"])
def FCgraph():
    call(["python3", "FCgraph.py"])

exitb = tk.Button(win,
        text="Exit",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 50,
        height = 15,              
        bg="light green",
        fg='white',
        command= exitProgram,
        activebackground="dark gray")
exitb.pack(side=BOTTOM,anchor=E,padx=5)
pHgraph = tk.Button(win,
        text="pHgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= pHgraph,
        activebackground="dark gray")
pHgraph.place(relx=0.02, rely=0.4)
ORPgraph = tk.Button(win,
        text="ORPgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= ORPgraph,
        activebackground="dark gray")
ORPgraph.place(relx=0.3, rely=0.4)
Tempgraph = tk.Button(win,
        text="Tempgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= Tempgraph,
        activebackground="dark gray")
Tempgraph.place(relx=0.3, rely=0.9)
DOgraph = tk.Button(win,
        text="DOgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= DOgraph,
        activebackground="dark gray")
DOgraph.place(relx=0.6, rely=0.4)
ECgraph = tk.Button(win,
        text="ECgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= ECgraph,
        activebackground="dark gray")
ECgraph.place(relx=0.02, rely=0.9)
Tempwert = gaugelib.DrawGauge2(
    win,
    max_value=50.0,
    min_value=-20.0,
    size=150,
    bg_col='black',
    unit = "Temp °C",bg_sel = 2)
Tempwert.place(relx=0.3, rely=0.5)
pHwert = gaugelib.DrawGauge2(
    win,
    max_value=14.0,
    min_value=0.0,
    size=150,
    bg_col='black',
    unit = "pH. ",bg_sel = 2)
pHwert.place(relx=0.02, rely=0.02)
ORPwert = gaugelib.DrawGauge2(
    win,
    max_value=2000.0,
    min_value=-2000.0,
    size=150,
    bg_col='black',
    unit = "ORP. mV",bg_sel = 2)
ORPwert.place(relx=0.3, rely=0.02)
DOwert = gaugelib.DrawGauge2(
    win,
    max_value=100.0,
    min_value=0.0,
    size=150,
    bg_col='black',
    unit = "DO. mg/L",bg_sel = 2)
DOwert.place(relx=0.6, rely=0.02)
ECwert = gaugelib.DrawGauge2(
    win,
    max_value=50.000,
    min_value=0.07,
    size=150,
    bg_col='black',
    unit = "EC. μS/cm",bg_sel = 2)
ECwert.place(relx=0.02, rely=0.5)
FCount = ThermometerLib.DrawBar(
    win,
    max_value=100,
    min_value=00,
    size=150,
    bg_col='black',
    unit = "Fishes")
FCount.place(relx=0.6, rely=0.5)
FCgraph = tk.Button(win,
        text="FCgraph",
        image=image,
        font=("Helvetica", 10,'bold'),
        compound="left",
        borderwidth=1,
        width = 150,
        height = 15,              
        bg="green",
        fg='white',
        command= FCgraph,
        activebackground="dark gray")
FCgraph.place(relx=0.6, rely=0.9)


class OneWire_Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.temp_max=0
        self.temp_min=100
        self.hum_max=0
        self.hum_min =100
        self.x=0
    def run(self):
        while self.x == 0:
            try:
                df = pd.read_csv("cpu.csv")
                Tempwert.set_value((df.iloc[-1][3]))
                pHwert.set_value((df.iloc[-1][1]))
                ORPwert.set_value((df.iloc[-1][2]))
                DOwert.set_value((df.iloc[-1][4]))
                ECwert.set_value((df.iloc[-1][5]))
                cf = pd.read_csv("fishcount.csv")
                FCount.set_value((cf.iloc[-1][1]))
                time.sleep(5)
            except:                                        
                print('Error2')
            pass
thread2 = OneWire_Thread()
thread2.start()
mainloop()
