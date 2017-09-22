import matplotlib.pyplot as plot
import copy
from InputReader import InputReader
class ImagePreprocessor(object):
    def __init__(self, image, coordinates):
        if(type(coordinates) is not tuple):
            print("WRONG COORDINATES!")
            return
        (x1, y1, x2, y2) = coordinates;
        width = x2-x1-1
        height = y2-y1-1
        self.oBitmap = [[0 for x in range(width+1)] for y in range(height+1)]
        for x in range(0, width):
            for y in range(0, height):
                    (red, green , blue)= image.getpixel((x,y))
                    self.oBitmap[y][x] = red
    def getBitmap(self):
        return self.oBitmap

    def thresholding(self, oInputBitmap, treshold=190):
        oInput = InputReader()
        height = len(oInputBitmap)
        width = len(oInputBitmap[0])
        oBitmap = [[0 for x in range(width+1)] for y in range(height+1)]
        while(True):
            print("Tresholding at",treshold,"treshold")
            for y in range(0, height):
                for x in range(0, width):
                    if oInputBitmap[y][x] > treshold:
                        oBitmap[y][x] = 255
                    else:
                        oBitmap[y][x] = 0
            plot.imshow(oBitmap, cmap='gray')
            plot.show(block=False)
            print("Press W/S to adjust treshold, press C to continue.")
            iReadkey = oInput.waitForAnyInput()
            if(iReadkey == 119):
                treshold+=10
                plot.close()
            if(iReadkey == 115):
                treshold-=10
                plot.close()
            if(iReadkey == 99):
                plot.close()
                break
        return oBitmap
