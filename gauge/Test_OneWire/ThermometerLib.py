import tkinter as tk
from tkinter import *
import cmath
import sys
import logging
import math
import time
from decimal import Decimal
from tkinter.font import Font
from tkinter import messagebox
import time
from time import sleep
import random

class ini(tk.Frame):
    def __init__(self, parent, size=100, **options):
        tk.Frame.__init__(self, parent, padx=0, pady=0, borderwidth=0,highlightthickness=0,
                          **options)
        self.size = size

class DrawBar(ini):
    def __init__(self, parent,
                 max_value: (float, int)=100.0,
                 min_value: (float, int)= 0.0,
                 size: (float, int)=100,
                 borderwidth: (float, int)= 0.0,
                 highlightthickness: (float, int)= 0.0,
                 bg_col:str='black',
                 unit: str=None,
                 **options):
        super().__init__(parent, size=size, **options)
        self.max_value = float(max_value)
        self.min_value = float(min_value)
        self.size = size
        self.bg_col = bg_col
        self.borderwidth = borderwidth
        self.highlightthickness= highlightthickness
        self.unit = '' if not unit else unit
        self.canvas = tk.Canvas(self, 
                    width=2*self.size/3,
                    height=self.size,
                    bg=self.bg_col,
                    highlightthickness= self.highlightthickness,
                    borderwidth=self.borderwidth)
        self.canvas.grid(row=0)
        self.draw_background()
        initial_value = 0.0
    def draw_background(self, divisions=100):
        self.dx=self.size/20
        self.dy = self.size/20
        y=self.size
        self.redx=6*self.dx
        self.redy=y-6*self.dx
        self.redw=2*self.dx
        self.diff = self.redy-2*self.dy
        self.range = int(self.max_value - self.min_value)
        self.tick = self.diff/ self.range
        self.arc1 = self.canvas.create_oval(4*self.dx,y-6*self.dx,10*self.dx, y,fill="red",width=0)
        self.canvas.create_text(7*self.dx,y-3*self.dx, font=("Arial",int(self.dx),'bold'),fill="orange", text='ProTerra')

        self.rect1 =self.canvas.create_rectangle(5*self.dx, y-5*self.dx, 9*self.dx, self.redy,fill = "red",width=0)
        self.rect2 =self.canvas.create_rectangle(5*self.dx, self.dy, 9*self.dx, self.redy,fill = "gray",width=0)
        self.rect =self.canvas.create_rectangle(self.redx, self.redy, self.redx+self.redw, 2*self.dy,fill = "light gray",width=0)
        self.rect3 =self.canvas.create_rectangle(self.redx, self.redy, self.redx+self.redw, self.redy-10,fill = "red",width=0)
        for t in range(self.range +1):
            if (t%10) == 0:
                label = str(self.min_value+t)
                self.canvas.create_text(2*self.dx,self.redy-t*self.tick, font=("Arial",int(5*self.dx/4),'bold'),fill="white", text=label,angle=0)                
                self.canvas.create_line(4*self.dx,self.redy-t*self.tick,6*self.dx,self.redy-t*self.tick,width=2,fill='white')
            elif (t%5) == 0:
                self.canvas.create_line(5*self.dx,self.redy-t*self.tick,6*self.dx,self.redy-t*self.tick,width=1,fill='white')
        label = str('%.2f' % 0)+"\n  "+ self.unit
        self.readout = self.canvas.create_text(11*self.dx,self.redy - 20, font=("Arial",int(self.dx),'bold'),fill="white", text=label,angle=0)
    def set_value(self, number):        
        number = number if number <= self.max_value else self.max_value
        number = number if number > self.min_value else self.min_value
        degree = (number - self.min_value) * self.tick        
        self.canvas.delete(self.rect3)
        self.rect3 =self.canvas.create_rectangle(self.redx, self.redy, self.redx+self.redw, self.redy-degree,fill = "red",width=0)
        label = str('%.2f' % number)  +"\n  "+ self.unit
        self.canvas.delete(self.readout)
        self.readout = self.canvas.create_text(11*self.dx,self.redy-degree, font=("Arial",int(self.dx),'bold'),fill="white", text=label,angle=0)
        