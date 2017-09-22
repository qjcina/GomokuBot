class ImagePreprocessor(object):

    def __init__(self, image, coordinates):
        if(type(coordinates) is not tuple):
            print("WRONG COORDINATES!")
            return
        (x1, y1, x2, y2) = coordinates;
        width = x2-x1-1
        height = y2-y1-1
        print(width,height)
        self.oBitmap = [[0 for y in range(height+1)] for x in range(width+1)] 
        for x in range(0, width):
            for y in range(0, height):
                 print(x,y)
                 (red, green , blue)= image.getpixel((x,y))
                 self.oBitmap[x][y] = (red+green+blue)/3
        
        print("debug")


