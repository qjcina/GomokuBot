import cv2
from .Settings import Settings
class BotMain(object):
    def __init__(self, oBitmap, oCoordinates):
        self.oBitmap = oBitmap
        self.oCoordinates = oCoordinates
        self.isReadyToExit = False
        #Algorithm for detecting line intersection
        #https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Mathematics
    def createMap(self, oBitmap):
        height = len(oBitmap)
        width = len(oBitmap[0])
        for y in range(0,height):
            for x in range(0,width):
                pass
    #Calculate intersection of 2 lines (defined by their 2 points)
    def getIntersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        y = ((x1 * y2 - y1 * x2)(y3 - y4) - (y1 - y2)(x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2)(x3 - x4))
        return (x,y)

    def process(self):
        oMapGenerator = Settings["mapGenerator"]
        while(True):

            if(self.isReadyToExit):
                break


