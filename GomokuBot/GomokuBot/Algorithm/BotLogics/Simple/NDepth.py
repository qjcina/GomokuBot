from Algorithm.BotLogics.Simple.ZeroDepth import ZeroDepth
from Resources.Resources import swapPlayer
class NDepth(ZeroDepth):
    def __init__(self, depth=5):
        self.iDepth = depth
        pass
    def logicLoop(self, oRawMap):        
        print("\nNDEPTH",self.iDepth, end = '\r')
        iCurrentDepth=0
        while(True):
            for halfTurn in [1, -0.1]:
                self.iMultiplier = halfTurn
                
                for y in range(0, len(oRawMap)):
                    for x in range(0,len(oRawMap[0])):
                        element = oRawMap[y][x]
                        if(iCurrentDepth<=0 and halfTurn==1):
                            if(element[2] != 0):
                                self.addAround(x,y, oRawMap) 
                            if(element[2] == self.iPlayer):
                                self.addAround(x, y, oRawMap)
                        self.checkInRow(x,y,oRawMap,5)
                        if(element[2] != 0):
                            self.oHeuristicMap[y][x] = -1000000
                            continue
                self.iPlayer = swapPlayer(self.iPlayer)
            iCurrentDepth+=1
            if(iCurrentDepth>=self.iDepth):
                break
