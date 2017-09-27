from Algorithm.MapGenerators.Map import Map, MapElement
class ZeroDepth(object):
    def __init__(self):
        pass
    def getPoint(self, oMap, iPlayer):
        self.iPlayer = iPlayer
        print("ZERODEPTH", end = '\r')
        if(isinstance(oMap, Map)):
            oMaximumValue = (0,None, None)
            oRawMap = oMap.getMap()
            self.oHeuristicMap = [[0 for i in range(0,len(oRawMap))] for j in range(0,len(oRawMap[0]))]
            for y in range(0, len(oRawMap)):
                for x in range(0,len(oRawMap[0])):
                    element = oRawMap[y][x]
                    self.addAround(x,y, oRawMap)
                    self.checkInRow(x,y,oRawMap,5)
                    if(element[2] != 0):
                        self.oHeuristicMap[y][x] = -100000
                        continue
            for y in range(0, len(oRawMap)):
                for x in range(0,len(oRawMap[0])):
                    if(self.oHeuristicMap[y][x] > oMaximumValue[0]):
                        oMaximumValue = (self.oHeuristicMap[y][x],oRawMap[y][x][0],oRawMap[y][x][1])
            return (oMaximumValue[1],oMaximumValue[2])

    def addToHeuristic(self, x,y, iAmount, oRawMap=None, iPlayer = None):    
        if(x < len(self.oHeuristicMap[0]) and y < len(self.oHeuristicMap) and x >= 0 and y >= 0):
            if(oRawMap[y][x][2]==iPlayer or oRawMap[y][x][2]==0 or iPlayer==None):
                self.oHeuristicMap[y][x]+=iAmount    
            if(oRawMap[y][x][2]==0):
                return True
            elif(oRawMap[y][x][2]!=iPlayer):
                return True
            return False
        return True

    def addAround(self, x, y, oRawMap):
        if(oRawMap[y][x][2]!=0):
            for i in range(-1,2):
                for j in range(-1,2):
                    self.addToHeuristic(x + j,y + i, 1, oRawMap)

    def checkInRow(self, x,y, oRawMap, iRange):
        power = iRange*2
        iDirection = 0
        if(self.iPlayer == oRawMap[y][x][2]):
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler==5):
                            power = 1000
                        else:
                            power = iRange*5
                        if(self.addToHeuristic(x + iDirection * iMultipler, y, power * iMultipler, oRawMap, self.iPlayer)):
                            break
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler==5):
                            power = 1000
                        else:
                            power = iRange*5
                        if(self.addToHeuristic(x, y + iDirection * iMultipler, power * iMultipler, oRawMap, self.iPlayer)):
                            break
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler==5):
                            power = 1000
                        else:
                            power = iRange*5
                        if(self. addToHeuristic(x + iDirection * iMultipler, y + iDirection * iMultipler, power * iMultipler, oRawMap, self.iPlayer)):
                            break
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    for iMultipler in range(1,iRange + 1):
                        if(iMultipler==5):
                            power = 1000
                        else:
                            power = iRange*5
                        if(self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * (-iMultipler), power * iMultipler, oRawMap, self.iPlayer)):
                            break
        elif(0 != oRawMap[y][x][2]):
            iColor = oRawMap[y][x][2]
            
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        if(iNumberInRow>=3):
                            power = 10000
                        else:
                            power = 0
                        if(self.addToHeuristic(x + iDirection * iMultipler, y, power, oRawMap, iColor)):
                                break
            
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        if(iNumberInRow>=3):
                            power = 10000
                        else:
                            power = 0
                        if(self.addToHeuristic(x, y + iDirection * iMultipler, power, oRawMap, iColor)):
                            break
            
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        if(iNumberInRow>=3):
                            power = 10000
                        else:
                            power = 0
                        if(self. addToHeuristic(x + iDirection * iMultipler, y + iDirection * iMultipler, power, oRawMap, iColor)):
                           break
            
            for iDirection in range(-1,2):
                if(iDirection != 0):
                    iNumberInRow = 0
                    for iMultipler in range(1,iRange + 1):
                        iNumberInRow+=1
                        if(iNumberInRow>=3):
                            power = 10000
                        else:
                            power = 0
                        if(self.addToHeuristic(x + iDirection * iMultipler, y + iDirection * (-iMultipler), power, oRawMap, iColor)):
                            break

    

