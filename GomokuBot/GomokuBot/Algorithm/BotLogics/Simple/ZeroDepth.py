from Algorithm.MapGenerators.Map import Map, MapElement
from Resources.DebugMemory import saveHeuristicMap
from random import randint
class ZeroDepth(object):
    def __init__(self):
        pass
    def getPoint(self, oMap, iPlayer):
        self.iPlayer = iPlayer
        oMultipleMaximumValues = [(0,0,0)]
        print("\nZERODEPTH", end = '\r')
        if(isinstance(oMap, Map)):
            oMaximumValue = (0,None, None)
            oRawMap = oMap.getMap()
            self.oHeuristicMap = [[0 for i in range(0,len(oRawMap))] for j in range(0,len(oRawMap[0]))]
            for y in range(0, len(oRawMap)):
                for x in range(0,len(oRawMap[0])):
                    element = oRawMap[y][x]
                    if(element[2] != 0):
                        self.addAround(x,y, oRawMap)             #adds 1 around each token
                    if(element[2] == self.iPlayer):
                        self.addAround(x, y, oRawMap)            #adds 1 more around his tokens
                    self.checkInRow(x,y,oRawMap,5)              #checks how many there are in row for opponent and himself
                    if(element[2] != 0):
                        self.oHeuristicMap[y][x] = -1000000
                        continue
            for y in range(0, len(oRawMap)):
                for x in range(0,len(oRawMap[0])):
                    if(self.oHeuristicMap[y][x] > oMultipleMaximumValues[0][0]):
                        oMultipleMaximumValues = []
                        oMultipleMaximumValues.append((self.oHeuristicMap[y][x],oRawMap[y][x][0],oRawMap[y][x][1]))
                    elif(self.oHeuristicMap[y][x] == oMultipleMaximumValues[0][0]):
                        oMultipleMaximumValues.append((self.oHeuristicMap[y][x],oRawMap[y][x][0],oRawMap[y][x][1]))
            oMaximumValue = oMultipleMaximumValues[randint(0,len(oMultipleMaximumValues) - 1)]
            saveHeuristicMap(self.oHeuristicMap, oRawMap)
            return (oMaximumValue[1],oMaximumValue[2])

    def addToHeuristic(self, x,y, iAmount, oRawMap=None, iPlayer=None):    
        if(x < len(self.oHeuristicMap[0]) and y < len(self.oHeuristicMap) and x >= 0 and y >= 0):
            if(oRawMap[y][x][2] == iPlayer or oRawMap[y][x][2] == 0 or iPlayer == None):
                self.oHeuristicMap[y][x]+=iAmount    
            if(oRawMap[y][x][2] == 0):
                return True
            elif(oRawMap[y][x][2] != iPlayer):
                return True
            return False
        return True

    def addAround(self, x, y, oRawMap):
        if(oRawMap[y][x][2] != 0):
            for i in range(-1,2):
                for j in range(-1,2):
                    self.addToHeuristic(x + j,y + i, 1, oRawMap)

    def checkColor(self, x, y, iColor, oRawMap):
        if(x < len(self.oHeuristicMap[0]) and y < len(self.oHeuristicMap) and x >= 0 and y >= 0):
            if(oRawMap[y][x][2] == iColor):
                return True
            else:
                return False
        return False

    def setPower(self, x, y, iNumberInRow, oRawMap):
        if(iNumberInRow >= 3):
            power = 10000
            if(x < len(self.oHeuristicMap[0]) and y < len(self.oHeuristicMap) and x >= 0 and y >= 0):
                if(oRawMap[y][x][2] == self.iPlayer and iNumberInRow < 4):
                    power = 50
        else:
            power = 0
        return power

    def checkInRow(self, x,y, oRawMap, iRange):
        power = iRange * 2
        iDirection = 0
        if(self.iPlayer == oRawMap[y][x][2]):
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler == 4):
                            power = 10000
                        else:
                            power = iRange * 5
                        if(self.addToHeuristic(x + iDirection * iMultipler, y, power * iMultipler, oRawMap, self.iPlayer)):
                            break
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler == 4):
                            power = 10000
                        else:
                            power = iRange * 5
                        if(self.addToHeuristic(x, y + iDirection * iMultipler, power * iMultipler, oRawMap, self.iPlayer)):
                            break
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler == 4):
                            power = 10000
                        else:
                            power = iRange * 5
                        if(self. addToHeuristic(x + iDirection * iMultipler, y + iDirection * iMultipler, power * iMultipler, oRawMap, self.iPlayer)):
                            break
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler == 4):
                            power = 10000
                        else:
                            power = iRange * 5
                        if(self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * (-iMultipler), power * iMultipler, oRawMap, self.iPlayer)):
                            break
        elif(0 != oRawMap[y][x][2]):
            iColor = oRawMap[y][x][2]
            
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        power = self.setPower(x - iDirection, y, iNumberInRow, oRawMap)
                        if(self.addToHeuristic(x + iDirection * iMultipler, y, power, oRawMap, iColor)):
                            #bot checks if there is gap in token placement
                            if(self.checkColor(x + iDirection * iMultipler, y, 0, oRawMap) and self.checkColor(x + iDirection * (iMultipler + 1), y, iColor, oRawMap)):
                                iNumberInRow+=1
                                power = self.setPower(x - iDirection, y, iNumberInRow, oRawMap)
                                self.addToHeuristic(x + iDirection * iMultipler, y, power, oRawMap, iColor) 
                            break
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        power = self.setPower(x, y - iDirection, iNumberInRow, oRawMap)
                        if(self.addToHeuristic(x, y + iDirection * iMultipler, power, oRawMap, iColor)):
                            #bot checks if there is gap in token placement
                            if(self.checkColor(x, y + iDirection * iMultipler, 0, oRawMap) and self.checkColor(x, y + iDirection * (iMultipler + 1), iColor, oRawMap)):
                                iNumberInRow+=1
                                power = self.setPower(x, y - iDirection, iNumberInRow, oRawMap)
                                self.addToHeuristic(x, y + iDirection * iMultipler, power, oRawMap, iColor) 
                            break
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        power = self.setPower(x - iDirection, y - iDirection, iNumberInRow, oRawMap)
                        if(self. addToHeuristic(x + iDirection * iMultipler, y + iDirection * iMultipler, power, oRawMap, iColor)):
                            #bot checks if there is gap in token placement
                            if(self.checkColor(x + iDirection * iMultipler, y + iDirection * iMultipler, 0, oRawMap) and self.checkColor(x + iDirection * (iMultipler + 1), y + iDirection * (iMultipler + 1), iColor, oRawMap)):
                                iNumberInRow+=1
                                power = self.setPower(x + iDirection * iMultipler, y - iDirection, iNumberInRow, oRawMap)
                                self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * iMultipler, power, oRawMap, iColor) 
                            break
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        power = self.setPower(x - iDirection, y + iDirection, iNumberInRow, oRawMap)
                        if(self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * (-iMultipler), power, oRawMap, iColor)):
                            #bot checks if there is gap in token placement
                            if(self.checkColor(x + iDirection * iMultipler, y + iDirection * (-iMultipler), 0, oRawMap) and self.checkColor(x + iDirection * (iMultipler + 1), y + iDirection * (-(iMultipler + 1)), iColor, oRawMap)):
                                iNumberInRow+=1
                                power = self.setPower(x - iDirection, y + iDirection, iNumberInRow, oRawMap)
                                self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * (-iMultipler), power, oRawMap, iColor) 
                            break

    

