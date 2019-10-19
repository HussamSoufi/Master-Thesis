import tkinter as tk
import cmath
import sys
import logging
import math
import time
from decimal import Decimal

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
                 pady: (float, int)=0,
                 padx: (float, int)=0,
                 img_data: str=None,
                 bg_col:str='blue',unit: str=None,bg_sel=1,
                 **options):
        super().__init__(parent, size=size, **options)
        self.max_value = float(max_value)
        self.min_value = float(min_value)
        self.size = size
        self.bg_col = bg_col
        self.bg_sel=bg_sel
        self.borderwidth = borderwidth
        self.highlightthickness= highlightthickness
        self.pady=pady
        self.padx=padx
        self.unit = '' if not unit else unit
        if self.bg_sel == 2:
            self.canvas = tk.Canvas(self, 
			width=self.size/2,
			height=self.size,
			bg=self.bg_col,
			highlightthickness=self.highlightthickness,
			borderwidth=self.borderwidth)
            self.canvas.grid(row=0,
			padx=self.padx,
			pady=self.pady)
        else:
            self.canvas = tk.Canvas(self, 
			width=self.size,
			height=self.size,
			bg=self.bg_col,
			highlightthickness= self.highlightthickness,
			borderwidth=self.borderwidth)
            self.canvas.grid(row=0,
			padx=self.padx,
			pady=self.pady)
        if bg_sel == 1:self.draw_background1()
        else:self.draw_background2()
        initial_value = 0.0
        
    def draw_background1(self, divisions=100):
        self.canvas.create_arc(self.size/7, self.size/7, 7 *self.size/8, 7 *self.size/8,
                       style="arc",width=self.size/4,start=0, extent=180,
                       outline = "dark blue")#style=tk.PIESLICE
        self.readout = self.canvas.create_text(self.size/2,4*self.size/5, font=("Arial",int(self.size/18),'bold'),fill="white", text='')

    def set_value(self, number: (float, int)):
        x0= self.size/7
        y0=self.size/7
        x1= 7 *self.size/8
        y1= 7 *self.size/8
        w = self.size/4
        dif=180
        max1 = 4*dif/5
        max2 = 3*dif/5
        max3 = 2*dif/5
        max4 = dif/5
        
        number = number if number <= self.max_value else self.max_value
        number = number if number > self.min_value else self.min_value
        degree = (number) / (self.max_value - self.min_value) * 180.0
        self.canvas.delete('all')
        self.canvas.create_arc(x0, y0, x1,y1,style="arc",width=w,start=0, extent=180,outline = "dark blue")#style=tk.PIESLICE
        if degree > max1:
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-degree, extent=degree-max1,outline = 'red')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max1, extent=max4,outline = 'tomato')
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max2, extent=max4,outline = 'peru')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max3, extent=max4,outline='gold')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max4,extent=max4,outline ='green')
        elif degree > max2:
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-degree, extent=degree-max4,outline = 'tomato')
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max2, extent=max4,outline = 'peru')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max3, extent=max4,outline='gold')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max4,extent=max4,outline ='green')
        elif degree > max3:
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-degree, extent=degree-max4,outline = 'peru')
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max3, extent=max4,outline = 'gold')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max4, extent=max4,outline='green')#style=tk.PIESLICE
        elif degree > max4:
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-degree, extent=degree,outline = 'gold')#style=tk.PIESLICE
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-max4, extent=max4,outline='green')#style=tk.PIESLICE
        else:
            self.bar=self.canvas.create_arc(x0,y0 ,x1 ,y1,style="arc",width=w,start=180-degree, extent=degree,outline = 'green')
        label = str('%.2f' % number)
        self.canvas.delete(self.readout)
        self.readout = self.canvas.create_text(self.size/2,4*self.size/5, font=("Arial",int(self.size/14),'bold'),fill="white", text=label,angle=0)

    def draw_background2(self, divisions=100):
        self.canvas.create_rectangle(self.size/7, self.size/7, self.size/2, 7*self.size/8,fill = "dark blue")
        self.readout = self.canvas.create_text(self.size/2,4*self.size/5, font=("Arial",int(self.size/18),'bold'),fill="white", text='')
    
    def set_value2(self, number: (float, int)):
        x0= self.size/7
        y0=self.size/7
        x1= 5 *self.size/8
        y1= 7*self.size/8
        dif=y1-y0
        max1 = 4*dif/5
        max2 = 3*dif/5
        max3 = 2*dif/5
        max4 = dif/5
        
        number = number if number <= self.max_value else self.max_value
        number = number if number > self.min_value else self.min_value
        degree = (number * dif) / (self.max_value - self.min_value)
        
        self.canvas.delete('all')
        self.canvas.create_rectangle(x0-2, y0-2, x1+2 , y1+2,fill = "dark blue")#style=tk.PIESLICE
        if degree > max1:
            self.canvas.create_rectangle(x0,y1-degree,x1,y1-max1,fill = "red",width=0)                  
            self.canvas.create_rectangle(x0,y1-max1,x1,y1-max2,fill = "tomato",width=0)                  
            self.canvas.create_rectangle(x0,y1-max2,x1,y1-max3,fill = "peru",width=0)                  
            self.canvas.create_rectangle(x0,y1-max3,x1,y1-max4,fill = "gold",width=0)                  
            self.canvas.create_rectangle(x0,y1-max4,x1,y1,fill = "green",width=0)                  
        elif degree > max2:
            self.canvas.create_rectangle(x0,y1-degree,x1,y1-max2,fill = "tomato",width=0)                  
            self.canvas.create_rectangle(x0,y1-max2,x1,y1-max3,fill = "peru",width=0)                  
            self.canvas.create_rectangle(x0,y1-max3,x1,y1-max4,fill = "gold",width=0)                  
            self.canvas.create_rectangle(x0,y1-max4,x1,y1,fill = "green",width=0)                  
        elif degree > max3:
            self.canvas.create_rectangle(x0,y1-degree,x1,y1-max3,fill = "peru",width=0)                  
            self.canvas.create_rectangle(x0,y1-max3,x1,y1-max4,fill = "gold",width=0)                  
            self.canvas.create_rectangle(x0,y1-max4,x1,y1,fill = "green",width=0)                  
        elif degree > max4:
            self.canvas.create_rectangle(x0,y1-degree,x1,y1-max4,fill = "gold",width=0)                  
            self.canvas.create_rectangle(x0,y1-max4,x1,y1,fill = "green",width=0)                  
        else:
            self.canvas.create_rectangle(x0,y1-degree,x1,y1,fill = "green",width=0)                  
        label = str('%.2f' % number)
        self.canvas.delete(self.readout)
        self.readout = self.canvas.create_text(x0 /2 + x1 / 2,y0-(self.size/14), font=("Arial",int(self.size/14),'bold'),fill="white", text=label,angle=0)
        