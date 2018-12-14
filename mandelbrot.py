import tkinter as tk
import math
import time
from scipy.interpolate import interp1d
import time
import colorsys

root = tk.Tk()
can = tk.Canvas(root, width=800, height=600, bg = "white")
can.grid()

f = 1
t = 1

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x*f-r+400, y*-f-r+300, x*f+r+400, y*-f+r+300, **kwargs)
tk.Canvas.create_circle = _create_circle

#origin = can.create_circle(0, 0, 2, fill="red", outline="red")

Sx = int(400/t)
Sy = int(300/t)


limit = 100
m = interp1d([1, limit+1], [0, 359])


def isMand(x, y):

    l = 0

    c = [[x, y]]
    
    r = c[0][0]
    i = c[0][1]

    nR = 0 # start number
    nI = 0 # start number

    while abs(nR) < 1e4:

        nRtemp = math.pow(nR, 2) + r - math.pow(nI, 2)
        nItemp = 2 * nR * nI + i

        nR = nRtemp
        nI = nItemp

        l += 1
        # print("---------------")
        # print("nR", nR)
        # print("nI", nI)
        # print("---------------")
        if l > 100:
            #print(l)
            break

    return l


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

for x in range(-1*Sx, Sx):
    x = x * 1/f
    for y in range(-1*Sy, Sy):
        y = y * 1/f
        iM = isMand(x, y)
        color = int(m(abs(iM)))
        print(x, y, iM, color)
        color = color/100
        
        colorRGB = hsv2rgb(color, 1, 0.9)

        # print(color)
        print(colorRGB)

        newColor = '#%02x%02x%02x' % colorRGB
        # newColor = '#%02x%02x%02x' % (color, color, color)

        can.create_circle(x, y, 2, fill=newColor, outline=newColor)

root.mainloop()