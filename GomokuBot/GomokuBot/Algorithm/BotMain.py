import cv2
import time
from Resources.DebugMemory import printHeuristicMap
from Resources.Resources import swapPlayer
from Resources.Settings import Settings
from Input.ColorGrabber import getPixelColor, getMapColors
from Input.MouseClicker import getCommandListener, MouseClicker
from Resources.Colors import getColor, Colors
from Algorithm.MapUpdate import updateMap, randomPosition, checkGameStatus
class BotMain(object):
    def __init__(self, oBitmap, oCoordinates):
        self.oBitmap = oBitmap
        self.oCoordinates = oCoordinates
        self.isReadyToExit = False
        self.oCommandListener = getCommandListener()
        self.oMouseClicker = MouseClicker()
        self.iWon = 0
        self.iLost = 0
    def process(self):
        oMapGenerator = Settings["mapGenerator"].value
        self.oMap = oMapGenerator.createMap(self.oBitmap, self.oCoordinates)
        oMenuGenerator = Settings["menuGenerator"].value
        oMenuPoints = oMenuGenerator.createMapPoints(self.oBitmap, self.oCoordinates)
        self.iSelectedSeat = self.selectSeat(oMenuPoints)
        self.iPlayer = None
        bStarted = False
        self.turn = 2
        bSomethingChanged = False
        bFirstTurn = True
        bSkipCheck = False
        botLogics = Settings["botLogics"].value
        while(True):
            if(bStarted == False and Colors.NonEmptySeat.name == getColor(getPixelColor(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1]))):
                self.oMouseClicker.tryClick(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1])
                time.sleep(5)
                print("WAITING FOR START")
            elif(bStarted == False and Colors.NonEmptySeat.name == getColor(getPixelColor(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1] + 10))):
                self.oMouseClicker.tryClick(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1] + 10)
                time.sleep(5)
                print("WAITING FOR START")
            elif(bStarted == False):
                print("Game started!")  
                bStarted = True
                if(1 == self.iSelectedSeat):
                    oPlayerColor = getColor(getPixelColor(oMenuPoints["player1Color"][0], oMenuPoints["player1Color"][1]))
                    if(oPlayerColor == Colors.Player1.name):
                        self.iPlayer = 2 #black
                    else:
                        self.iPlayer = 1 #white
                elif(2 == self.iSelectedSeat):
                    oPlayerColor = getColor(getPixelColor(oMenuPoints["player2Color"][0], oMenuPoints["player2Color"][1]))
                    if(oPlayerColor == Colors.NonEmptySeat.name):
                        self.iPlayer = 1 #black
                    else:
                        self.iPlayer = 2 #white
                else:
                    return False
                print("SELECTED SIDE:", self.iPlayer)
            if(bStarted):
                print("Turn",self.turn,"Player",self.iPlayer,end='\r')
                self.oRefreshMap = getMapColors(self.oMap.get2DArray())
                if(checkGameStatus(self.oMap, self.oRefreshMap)):
                    bStarted = False
                    if(botLogics.bWinningCondition):
                        self.iWon+=1
                    else:
                        self.iLost+=1
                    continue
                if(bSkipCheck):
                    updateMap(self.oMap, self.oRefreshMap, self.iPlayer)
                    bSkipCheck = False
                else:
                    bSomethingChanged = updateMap(self.oMap, self.oRefreshMap, self.iPlayer)

                if(bSomethingChanged == True and self.turn != self.iPlayer):
                    self.turn = swapPlayer(self.turn)
                    bFirstTurn = False
                elif(self.turn == self.iPlayer):
                    if(bFirstTurn):
                        (iXClick, iYClick) = randomPosition(self.oMap)
                    else:
                        (iXClick, iYClick) = botLogics.getPoint(self.oMap, self.iPlayer)
                    self.oMouseClicker.tryClick(iXClick, iYClick)
                    self.turn = swapPlayer(self.iPlayer)
                    bFirstTurn = False
                    bSomethingChanged = False
                    bSkipCheck = True
                    

            if(self.isReadyToExit):
                break
    def selectSeat(self, oMenuPoints):
        if(self.clickSeat(oMenuPoints["player1Position"])):
            return 1
        elif(self.clickSeat(oMenuPoints["player2Position"])):
            return 2
        return 0
            
    def clickSeat(self, oClickPoint):
        if(Colors.EmptySeat.name == getColor(getPixelColor(oClickPoint[0], oClickPoint[1]))):
            self.oMouseClicker.tryClick(oClickPoint[0], oClickPoint[1])
            return True
        return False

