import matplotlib.pyplot as plot
from Input import ColorGrabber
from Resources.Colors import Colors, getColor
from Algorithm.MenuGenerators.Menu import Menu
class BrightnessMapGenerator(object):
    def __init__(self):
        pass
    def detectMenuPosition(self, width, height, oBitmap):
        iFollowingPoints = 0
        iMenuStart = None
        iMenuEnd = None
        iVerticalAverage = [0 for i in range(0, width)]
        for x in range(0,width):
            for y in range(0,height):
                if(oBitmap[y][x] == 255):
                    iVerticalAverage[x]+=255
            iVerticalAverage[x]/=height
        for x in range(0,width):
            if(iVerticalAverage[x] < 50):
                iFollowingPoints+=1
            else:
                iFollowingPoints = 0
            if(iFollowingPoints > 5 and iMenuStart is None):
                iMenuStart = x
                break
        iFollowingPoints = 0
        for x in range(0,width):
            if(iVerticalAverage[width - 1 - x] < 50):
                iFollowingPoints+=1
            else:
                iFollowingPoints = 0
            if(iFollowingPoints > 5 and iMenuEnd is None):
                iMenuEnd = width - 1 - x
                break
        if(iMenuEnd - iMenuStart < 100):
            iMenuEnd = width
        return iMenuEnd, iMenuStart

    def separateMenu(self, height, oBitmap, iMenuEnd, iMenuStart):
        oMenuBitmap = [None for i in range(0, height)]
        for y in range(0,height):
            oMenuBitmap[y] = oBitmap[y][iMenuStart:iMenuEnd]
        height = len(oMenuBitmap)
        width = len(oMenuBitmap[0])
        return height, oMenuBitmap, width

    def calculateHorizontalAverages(self, height, width, oMenuBitmap):
        iHorizontalAverage = [0 for i in range(0, height)]
        for y in range(0,height):
            for x in range(0,width):
                if(oMenuBitmap[y][x] == 255):
                    iHorizontalAverage[y]+=255
            iHorizontalAverage[y]/=height
        return iHorizontalAverage

    def findPlayerButtons(self, height, iHorizontalAverage):
        iPlayerButtonsStart = None
        iPlayerButtonsEnd = None
        iFollowingPoints = 0
        for y in range(0,height):
            if(iHorizontalAverage[y] > 50):
                iFollowingPoints+=1
                if(iFollowingPoints > 5 and iPlayerButtonsStart == None):
                    iPlayerButtonsStart = y - 5
            else:
                if(iPlayerButtonsStart is not None):
                    iPlayerButtonsEnd = y
                else:
                    iFollowingPoints = 0
        return iPlayerButtonsStart, iPlayerButtonsEnd

    def createMapPoints(self, oBitmap, oCoordinates):
        height = len(oBitmap)
        width = len(oBitmap[0])
        iFollowingPoints = 0
        iMenuEnd, iMenuStart = self.detectMenuPosition(width, height, oBitmap)
        iStartPosition = (iMenuStart / 2, -20 + (height / 2))
        height, oMenuBitmap, width = self.separateMenu(height, oBitmap, iMenuEnd, iMenuStart)
        iHorizontalAverage = self.calculateHorizontalAverages(height, width, oMenuBitmap)
        iPlayerButtonsStart, iPlayerButtonsEnd = self.findPlayerButtons(height, iHorizontalAverage)

        (iXLeftSeat, iYLeftSeat) = (len(oMenuBitmap[0]) / 3 + iMenuStart, iPlayerButtonsStart + 2)
        strColor = getColor(ColorGrabber.getPixelColor(iXLeftSeat, iYLeftSeat, True, oCoordinates))
        iLeftSeat = None
        iRightSeat = None
        if(strColor == "EmptySeat" or strColor == "NonEmptySeat"):
            iLeftSeat = (iXLeftSeat, iYLeftSeat)
        (iXRightSeat, iYRightSeat) = ((len(oMenuBitmap[0]) / 3) * 2 + iMenuStart, iPlayerButtonsStart + 2)
        strColor = getColor(ColorGrabber.getPixelColor(iXRightSeat, iYRightSeat, True, oCoordinates))
        if(strColor == "EmptySeat" or strColor == "NonEmptySeat"):
            iRightSeat = (iXRightSeat, iYRightSeat)
        return Menu(iLeftSeat,iRightSeat,iStartPosition,True,oCoordinates)



