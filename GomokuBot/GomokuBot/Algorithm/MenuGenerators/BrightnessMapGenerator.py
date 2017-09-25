import matplotlib.pyplot as plot
from Input import ColorGrabber
from Resources.Colors import Colors, getColor
class BrightnessMapGenerator(object):
    def __init__(self):
        pass
    def createMapPoints(self, oBitmap, oCoordinates):
        height = len(oBitmap)
        width = len(oBitmap[0])
        iVerticalAverage = [0 for i in range(0, width)]
        iFollowingPoints = 0
        iMenuStart = None
        iMenuEnd = None
        for iXLeftSeat in range(0,width):
            for iYLeftSeat in range(0,height):
                if(oBitmap[iYLeftSeat][iXLeftSeat] == 255):
                    iVerticalAverage[iXLeftSeat]+=255
            iVerticalAverage[iXLeftSeat]/=height
        for iXLeftSeat in range(0,width):
            if(iVerticalAverage[iXLeftSeat] < 50):
                iFollowingPoints+=1
            else:
                iFollowingPoints = 0
            if(iFollowingPoints > 5 and iMenuStart is None):
                iMenuStart = iXLeftSeat
                break
        iFollowingPoints = 0
        for iXLeftSeat in range(0,width):
            if(iVerticalAverage[width - 1 - iXLeftSeat] < 50):
                iFollowingPoints+=1
            else:
                iFollowingPoints = 0
            if(iFollowingPoints > 5 and iMenuEnd is None):
                iMenuEnd = width - 1 - iXLeftSeat
                break
        if(iMenuEnd - iMenuStart < 100):
            iMenuEnd = width
        iStartPosition = (iMenuStart / 2, height / 2)
        oMenuBitmap = [None for i in range(0, height)]
        for iYLeftSeat in range(0,height):
            oMenuBitmap[iYLeftSeat] = oBitmap[iYLeftSeat][iMenuStart:iMenuEnd]
        height = len(oMenuBitmap)
        width = len(oMenuBitmap[0])
        iHorizontalAverage = [0 for i in range(0, height)]
        for iYLeftSeat in range(0,height):
            for iXLeftSeat in range(0,width):
                if(oMenuBitmap[iYLeftSeat][iXLeftSeat] == 255):
                    iHorizontalAverage[iYLeftSeat]+=255
            iHorizontalAverage[iYLeftSeat]/=height
        plot.imshow(oBitmap, cmap='gray')
        iPlayerButtonsStart = None
        iPlayerButtonsEnd = None
        iFollowingPoints = 0
        for iYLeftSeat in range(0,height):
            if(iHorizontalAverage[iYLeftSeat] > 50):
                iFollowingPoints+=1
                if(iFollowingPoints > 5 and iPlayerButtonsStart == None):
                    iPlayerButtonsStart = iYLeftSeat - 5
            else:
                if(iPlayerButtonsStart is not None):
                    iPlayerButtonsEnd = iYLeftSeat
                else:
                    iFollowingPoints = 0
        oMenuBitmap[:] = [item for item in oMenuBitmap if item != []]
        (iXLeftSeat, iYLeftSeat) = (len(oMenuBitmap[0]) / 3 + iMenuStart, iPlayerButtonsStart + 2)
        strColor = getColor(ColorGrabber.getPixelColor(iXLeftSeat, iYLeftSeat, True, oCoordinates))
        iLeftSeat = None
        iRightSeat = None
        if(strColor == "EmptySeat" or strColor == "nonEmptySeat"):
            iLeftSeat = (iXLeftSeat, iYLeftSeat)
        (iXRightSeat, iYRightSeat) = ((len(oMenuBitmap[0]) / 3)*2 + iMenuStart, iPlayerButtonsStart + 2)
        strColor = getColor(ColorGrabber.getPixelColor(iXLeftSeat, iYLeftSeat, True, oCoordinates))
        if(strColor == "EmptySeat" or strColor == "nonEmptySeat"):
            iRightSeat = (iXRightSeat, iYRightSeat)
        plot.scatter(iXRightSeat, iYRightSeat)
        plot.scatter(iXLeftSeat, iYLeftSeat)
        plot.show()
        pass



