#!/bin/python
import tkinter as tk
import math
import time
from scipy.interpolate import interp1d
import time
import colorsys
import datetime
from multiprocessing import Pool
from PIL import Image
import numpy as np

#def _create_circle(self, x, y, r, **kwargs):
    ## return self.create_oval((x+xOffset)*z-r+width, y*-z-r+height, (x+xOffset)*z+r+width, y*-z+r+height, **kwargs)
    ##x = xa*z
    ##y = ya*z
    #x = x/g
    #y = y/g
    
    #return self.create_oval(x - r + width + xOffset, y - r + height + yOffset, x + r + width + xOffset, y + r + height + yOffset, **kwargs)

#tk.Canvas.create_circle = _create_circle

def makePixel(x, y, color):
    # return self.create_oval((x+xOffset)*z-r+width, y*-z-r+height, (x+xOffset)*z+r+width, y*-z+r+height, **kwargs)
    #x = xa*z
    #y = ya*z
    
    x = x/g
    y = y/g
    
    x = x + width #+ xOffset
    y = y + height #+ yOffset

    try:
        pix[x, y] = color
    except IndexError:
        abc = 0

def isMand(x, y):

    x = x/z+xOffset
    y = y/z

    l = 0

    c = [[x, y]]
    
    r = c[0][0]
    i = c[0][1]

    nR = 0 # start number
    nI = 0 # start number

    while abs(nR) < 1e3:

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


def doWork(part):
    #windowUpdate = 0
    xSlice = 0

    if part == 1:
        r1 = -1*Sx
        r2 = -1*Sx/2
    elif part == 2:
        r1 = -1*Sx/2
        r2 = 0
    elif part == 3:
        r1 = 0
        r2 = Sx/2
    elif part == 4:
        r1 = Sx/2
        r2 = Sx
    
    status = 0
    
    brotNumbers = []
    #for xt in range(int(r1), int(r2)):
    for xt in np.arange(r1, r2, g):
        #for x in range(xt, xt*g):
        for x in np.arange(xt, xt+g, g):
            
            ta = datetime.datetime.now()
            
            #for x in range(x, 
            #x = x * f
            status = round(xSlice/(abs(r2-r1))*100, 2)
            
            #for yt in range(-1*Sy, Sy):
            for yt in np.arange(-1*Sy, Sy, g):
                #for y in range(yt, yt*g):
                for y in np.arange(yt, yt+g, g):
                    #print(part, status, '% | Current y:', int(currentY(y)), '%')
                    #y = y * f
                    iM = isMand(x, y)
                    color = int(m(abs(iM)))
                    
                    color = color/100
                    
                    colorRGB = hsv2rgb(color, 1, 0.9)
    
                    colorHex = '#%02x%02x%02x' % colorRGB
    
                    # can.create_circle(x, y, 1, fill=colorHex, outline=colorHex) # create a dot
                    brotNumbers.append((x, y, colorHex, colorRGB))
                    
                    #windowUpdate += 1
                    #if windowUpdate >= 1000:
                        #windowUpdate = 0
                        #root.update() # how often the window updates
                        
        tb = datetime.datetime.now()
        print(z, "calculating part", part, ":", status, "%")
        partStatus[part-1] = status
        #print("Part 1:", partStatus[0], "Part 2:", partStatus[1], "Part 3:", partStatus[2], "Part 4:", partStatus[3], end='\r')
        #print("Part", part, "1", r1, "2", r2)
        tT  = tb - ta
        
        #print("Remaining Time: ", tT * (abs(r2-r1)-xSlice))
        xSlice += g
        
    print("returning numbers...")
    
    return brotNumbers

   
if __name__ == '__main__':
    for z in np.arange(1000, 50000, 100):
    #for z in range(1):

        g = 1
        name = str(g)

        width = 400
        height = 300

        Sx = int(width)
        Sy = int(height)

        #root = tk.Tk()
        #can = tk.Canvas(root, width=width*2, height=height*2, bg = "white")
        #can.pack()
        #root.update()

        newImg = Image.new("RGB", (width*2, height*2))
        pix = newImg.load()

        #f = 0.01 # point per pixel 0.05
        #z = 500 # zoom 50
        #t = 1 # size 10
        #g = 1/500 # gap to fill

        xOffset = -0.75
        yOffset = 0
        
        currentY = interp1d([-1*Sy, Sy], [0, 100])

        partStatus = [0, 0, 0, 0]

        limit = 100
        m = interp1d([1, limit+1], [0, 359])
        
        pool = Pool(4)
        numbers = pool.map(doWork, (1, 2, 3, 4))    

        #print(numbers)
        print("building image...")
        for package in numbers:
            for n in package:
                x = n[0]
                y = n[1]
                colorHex = n[2]
                #can.create_circle(x, y, 1, fill=colorHex, outline=colorHex) # create a dot
                #root.update()
                makePixel(x, y, n[3])
                
        print("ready")
        #newImg.save("output/image" + name + ".png")
        newImg.save("output/image"+ str(z) +".png")
        print("image ready")
    
    #root.update()
    #root.mainloop()
