import matplotlib.pyplot as plot
import matplotlib.lines as mlines
class LineMapGenerator(object):
    debug = False
    def __init__(self):
        pass

    def setDebug(self):
        self.debug = True

    def countPositivePixels(self, height, iHorizontalAverage, iVerticalAverage, oBitmap, width):
        for y in range(0,height):
            for x in range(0,width):
                if(oBitmap[y][x] == 255):
                    iVerticalAverage[x]+=255
                    iHorizontalAverage[y]+=255

    def calculateAverage(self, iElementsNumber, oAverageList):
        for x in range(0,len(oAverageList)):
            oAverageList[x]/=iElementsNumber
            if(oAverageList[x] < 128):
                oAverageList[x] = 0
            else:
                oAverageList[x] = 255

    def findLines(self, iVerticalAverage):
        iFollowingZeros = 0
        oLines = []
        for x in range(0,len(iVerticalAverage)):
            if(iVerticalAverage[x] == 0):
                iFollowingZeros+=1
            else:
                if(iFollowingZeros > 0):
                    oLines.append(x)
                iFollowingZeros = 0
        print("Found",len(oLines),"lines")
        return oLines

    def createMap(self, oBitmap, oCoordinates):
        height = len(oBitmap)
        width = len(oBitmap[0])
        iVerticalAverage = [0 for i in range(0, width)]
        iHorizontalAverage = [0 for i in range(0, height)]
        self.countPositivePixels(height, iHorizontalAverage, iVerticalAverage, oBitmap, width)
        self.calculateAverage(height, iVerticalAverage)
        oVerticalLines = self.findLines(iVerticalAverage)
        iLastVerticalLine = max(oVerticalLines)
        del iHorizontalAverage[iLastVerticalLine+10:]
        self.calculateAverage(width, iHorizontalAverage)
        oHorizontalLines = self.findLines(iHorizontalAverage)

        if(self.debug == True):
            self.__showDebug(oBitmap, oVerticalLines, oHorizontalLines, width, height)

    def __showDebug(self, oBitmap, oVerticalLines, oHorizontalLines, width, height):
        plot.imshow(oBitmap)
        for x in range(0,len(oVerticalLines)):
            line = mlines.Line2D([oVerticalLines[x], oVerticalLines[x]],[0,height])
            plotGCA = plot.gca()
            plotGCA.add_line(line)
        for x in range(0,len(oHorizontalLines)):
            line = mlines.Line2D([0,width],[oHorizontalLines[x], oHorizontalLines[x]])
            plotGCA = plot.gca()
            plotGCA.add_line(line)
        plot.show()
    #Algorithm for detecting line intersection
    #https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Mathematics
    #Calculate intersection of 2 lines (defined by their 2 points)
    def getIntersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        y = ((x1 * y2 - y1 * x2)(y3 - y4) - (y1 - y2)(x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2)(x3 - x4))
        return (x,y)



