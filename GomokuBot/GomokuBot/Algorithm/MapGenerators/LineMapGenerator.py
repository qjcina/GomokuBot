import matplotlib.pyplot as plot

class LineMapGenerator(object):
    def __init__(self):
        pass
    def createMap(self, oBitmap):
        height = len(oBitmap)
        width = len(oBitmap[0])
        iVerticalAverage = [0 for i in range(0, width)]
        iHorizontalAverage = [0 for i in range (0, height)]
        for y in range(0,height):
            for x in range(0,width):
                if(oBitmap[y][x]==255):
                    iVerticalAverage[x]+=255
        for x in range(0,width):
            iVerticalAverage[x]/=height
            if(iVerticalAverage[x]<128):
                iVerticalAverage[x]=0
            else:
                iVerticalAverage[x]=255
        

        plot.plot(iVerticalAverage)
        plot.show()
    #Algorithm for detecting line intersection
    #https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Mathematics
    #Calculate intersection of 2 lines (defined by their 2 points)
    def getIntersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        y = ((x1 * y2 - y1 * x2)(y3 - y4) - (y1 - y2)(x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2)(x3 - x4))
        return (x,y)



