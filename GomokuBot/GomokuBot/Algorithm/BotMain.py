import cv2
from Resources.Settings import Settings
from Input.ColorGrabber import getPixelColor
from Input.MouseClicker import getCommandListener, MouseClicker
from Resources.Colors import getColor, Colors
class BotMain(object):
    def __init__(self, oBitmap, oCoordinates):
        self.oBitmap = oBitmap
        self.oCoordinates = oCoordinates
        self.isReadyToExit = False
        self.oCommandListener = getCommandListener()
        self.oMouseClicker = MouseClicker()

    def process(self):
        oMapGenerator = Settings["mapGenerator"].value
        self.oMap = oMapGenerator.createMap(self.oBitmap, self.oCoordinates)
        oMenuGenerator = Settings["menuGenerator"].value
        oMenuPoints = oMenuGenerator.createMapPoints(self.oBitmap, self.oCoordinates)
        self.iSelectedSeat = self.selectSeat(oMenuPoints)
        if(1==self.iSelectedSeat):
            oPlayerColor = getColor(getPixelColor(oMenuPoints["player1Color"][0], oMenuPoints["player1Color"][1]))
            if(oPlayerColor == Colors.Player1.name):
                self.iPlayer = 1 #black
            else:
                self.iPlayer = 2 #white
        elif(2==self.iSelectedSeat):
            oPlayerColor = getColor(getPixelColor(oMenuPoints["player2Color"][0], oMenuPoints["player2Color"][1]))
            if(oPlayerColor == Colors.NonEmptySeat.name):
                self.iPlayer = 1 #black
            else:
                self.iPlayer = 2 #white
        else:
            return False
        while(True):
            if(Colors.EmptySeat.name==getColor(getPixelColor(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1]))):
                self.oMouseClicker.tryClick(oMenuPoints["startPosition"][0], oMenuPoints["startPosition"][1])
            for y in self.oMap.oMap:
                for x in y:
                    x = getColor(getPixelColor(self.oMap.oMap[y],[x]))

            if(self.isReadyToExit):
                break
    def selectSeat(self, oMenuPoints):
        if(self.clickSeat(oMenuPoints["player1Position"])):
            return 1
        elif(self.clickSeat(oMenuPoints["player2Position"])):
            return 2
        return 0
            
    def clickSeat(self, oClickPoint):
        if(Colors.EmptySeat.name==getColor(getPixelColor(oClickPoint[0], oClickPoint[1]))):
            self.oMouseClicker.tryClick(oClickPoint[0], oClickPoint[1])
            return True
        return False

