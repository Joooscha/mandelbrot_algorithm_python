import tkinter as tk
import math
import time
from scipy.interpolate import interp1d
import time

# while nR+nI < 1e3:
#     #n = math.pow(n + 1, 2) + -1.5 + 1
    
#     nRtemp = math.pow(nR, 2) + r - math.pow(nI, 2)
#     nItemp = 2 * nR * nI + i

#     nR = nRtemp
#     nI = nItemp

#     l += 1
#     print("---------------")
#     print("nR", nR)
#     print("nI", nI)
#     print("---------------")
#     if l > limit:
#         print(l)
#         break

root = tk.Tk()
can = tk.Canvas(root, width=800, height=600, bg = "white")
can.grid()

f = 10

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x*f-r+400, y*-f-r+300, x*f+r+400, y*-f+r+300, **kwargs)
tk.Canvas.create_circle = _create_circle

origin = can.create_circle(0, 0, 2, fill="red", outline="red")

Sx = int(4000)
Sy = int(3000)


limit = 100
m = interp1d([0, limit+1], [0, 255])


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
            print(l)
            break

    return l



for x in range(-1*Sx, Sx):
    x = x * 0.1
    for y in range(-1*Sy, Sy):
        y = y * 0.1
        iM = isMand(x, y)
        color = int(m(abs(iM)))
        print(x, y, iM, color)
        color = 255 - color
        upColor = '#%02x%02x%02x' % (color, color, color)

        can.create_circle(x, y, 2, fill=upColor, outline=upColor)

root.mainloop()

'''

c = int(m(x))
color = '#%02x%02x%02x' % (c, c, c)
can.create_circle(math.cos(math.pi/180*x)*50, math.sin(math.pi/180*x)*50, 5, fill=color, outline=color)

'''