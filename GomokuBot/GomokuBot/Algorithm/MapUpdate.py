from Resources.Colors import Colors, getColor
from Input.ColorGrabber import treshold, getMapColors, getPixelColor
from random import randint
from Algorithm.MapGenerators.Map import *
def updateMap(oMap, tiColors, iPlayer):
    iColorIterator = 0
    bChanged = False
    if isinstance(oMap, Map):
        for y in oMap.oMap:
            for element in y:
                oColor = getColor(treshold(tiColors[iColorIterator]))
                if(oColor == Colors.Black.name):
                    if(element.iPlayerToken != 1):
                        element.iPlayerToken = 1
                        bChanged = True
                elif(oColor == Colors.NonEmptySeat.name):
                    if(element.iPlayerToken != 2):
                        element.iPlayerToken = 2
                        bChanged = True
                elif(oColor == Colors.LastMove.name):
                    element.iPlayerToken = iPlayer
                    bChanged = True
                else: 
                    element.iPlayerToken = 0
                iColorIterator+=1
    return bChanged
def randomPosition(oMap, bIsOccupied=False):
    if(isinstance(oMap, Map)):
        (xlen, ylen) = oMap.getLength()
        while(True):
            oRandomizedPoint = oMap.oMap[randint(0,ylen - 1)][randint(0,xlen - 1)]
            if(oRandomizedPoint.iPlayerToken != 0 and bIsOccupied == False):
                continue
            break
        return (oRandomizedPoint.iXPosition, oRandomizedPoint.iYPosition)


