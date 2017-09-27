from Algorithm.MapGenerators.MapElement import MapElement
import matplotlib.pyplot as plot
class Map(object):
    def __init__(self, oPoints, iSize, oCoordinates = None, bArePointsRelative = True):
        #Create blank map
        self.oMap = [[None for i in range(0,iSize[1])] for i in range(0,iSize[0])]
        oAbsolutePoints = []
        for point in oPoints:
            if(bArePointsRelative is True):
                [x,y] = point
                oAbsolutePoints.append([x+oCoordinates[0], y+oCoordinates[1]])
            else:
                oAbsolutePoints.append(point)
        i=0
        for y in range(0,len(self.oMap[0])):
            for x in range(0,len(self.oMap)):
                self.oMap[y][x] = MapElement(oAbsolutePoints[i][0],oAbsolutePoints[i][1])
                #plot.plot(oAbsolutePoints[i][0],oAbsolutePoints[i][1], marker="o")
                i+=1
    def get2DArray(self):
        oReturnArray = []
        for y in self.oMap:
            for x in y:
                oReturnArray.append((x.iXPosition, x.iYPosition))
        return oReturnArray
    def getMap(self):
        oReturnMap = [[None for i in range(0,len(self.oMap[0]))] for i in range(0,len(self.oMap))]
        for y in range(0,len(self.oMap)):
            for x in range(0,len(self.oMap[0])):
                oReturnMap[y][x] = (self.oMap[y][x].iXPosition, self.oMap[y][x].iYPosition, self.oMap[y][x].iPlayerToken)
        return oReturnMap
    def getLength(self):
        return (len(self.oMap[0]), len(self.oMap))

