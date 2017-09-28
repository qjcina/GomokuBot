import matplotlib.pyplot as plot
import matplotlib.lines as mlines
from Algorithm.MapGenerators.Map import Map
class LineMapGenerator(object):
    debug = False
    iMinSpacing = None
    def __init__(self):
        pass

    def setDebug(self):
        self.debug = True

    def countPositivePixels(self, height, iHorizontalAverage, iVerticalAverage, oBitmap, width):
        for y in range(0,height):
            for x in range(0,width):
                if(oBitmap[y][x] == 255):
                    iVerticalAverage[y]+=255
                    iHorizontalAverage[x]+=255

    def calculateAverage(self, iElementsNumber, oAverageList):
        for x in range(0,len(oAverageList)):
            oAverageList[x]/=iElementsNumber
            if(oAverageList[x] < 110):
                oAverageList[x] = 0
            else:
                oAverageList[x] = 255

    def findLines(self, iVerticalAverage):
        iFollowingZeros = 0
        self.iMinSpacing=None
        oLines = []
        for x in range(0,len(iVerticalAverage)):
            if(iVerticalAverage[x] == 0):
                iFollowingZeros+=1
            else:
                if(iFollowingZeros > 0):
                    if((self.iMinSpacing==None) or (x - oLines[-1] > self.iMinSpacing * 0.8)):
                        oLines.append(x)
                        if(self.iMinSpacing == None and len(oLines)  == 2):
                            self.iMinSpacing = oLines[1] - oLines[0] 
                iFollowingZeros = 0
        print("Found",len(oLines),"lines")
        return oLines

    def createMap(self, oBitmap, oCoordinates):
        height = len(oBitmap)
        width = len(oBitmap[0])
        iVerticalAverage = [0 for i in range(0, height)]
        iHorizontalAverage = [0 for i in range(0, width)]
        self.countPositivePixels(height, iHorizontalAverage, iVerticalAverage, oBitmap, width)
        self.calculateAverage(width, iVerticalAverage)
        oVerticalLines = self.findLines(iVerticalAverage)
        iLastVerticalLine = max(oVerticalLines)
        del iHorizontalAverage[iLastVerticalLine + 10:]
        self.calculateAverage(height, iHorizontalAverage)
        oHorizontalLines = self.findLines(iHorizontalAverage)
        if(len(oHorizontalLines)>len(oVerticalLines)):
            #Adds missing middle line
            oVerticalLines.insert(7,sum(oVerticalLines[6:8])/2)
        #Creates list of points.
        oPointsList = []
        for y in range(0,len(oVerticalLines)):
            for x in range(0,len(oHorizontalLines)):
                oPointsList.append([oHorizontalLines[x], oVerticalLines[y]])
        
        if(False):
            self.__showDebug(oBitmap, oVerticalLines, oHorizontalLines, width, height, oPointsList)
        
        return Map(oPointsList,(len(oHorizontalLines),len(oVerticalLines)), oCoordinates, True)

    def __showDebug(self, oBitmap, oVerticalLines, oHorizontalLines, width, height, oPoints):
        plot.imshow(oBitmap, cmap='gray')
        for x in range(0,len(oVerticalLines)):
            line = mlines.Line2D([0,width], [oVerticalLines[x], oVerticalLines[x]])
            plotGCA = plot.gca()
            plotGCA.add_line(line)
        for x in range(0,len(oHorizontalLines)):
            line = mlines.Line2D([oHorizontalLines[x], oHorizontalLines[x]],[0,height])
            plotGCA = plot.gca()
            plotGCA.add_line(line)
        x_list = [x for [x, y] in oPoints]
        y_list = [y for [x, y] in oPoints]
        plot.scatter(x_list, y_list)
        plot.show()
    #Algorithm for detecting line intersection
    #https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Mathematics
    #Calculate intersection of 2 lines (defined by their 2 points)
    def getIntersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        y = ((x1 * y2 - y1 * x2)(y3 - y4) - (y1 - y2)(x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2)(x3 - x4))
        return (x,y)



