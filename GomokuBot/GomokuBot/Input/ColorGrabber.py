import pyscreenshot as ImageGrab

def getPixelColor(i_x, i_y, bIsRelative=False, oCoordinates=(0,0,0,0)):
    if(bIsRelative is True):
        i_x += oCoordinates[0]
        i_y += oCoordinates[1]
    return ImageGrab.grab().load()[i_x, i_y]
def getMapColors(tiPoints):
    oImage = ImageGrab.grab().load()
    tiColorList = []
    for point in tiPoints:
        tiColorList.append(oImage[point[0], point[1]])
    return tiColorList
def treshold(tiColor):
    iSum = 0
    iBlackCount = iWhiteCount = 0
    for color in tiColor:
        if(color > 200):
            iWhiteCount+=1
        if(color < 50):
            iBlackCount+=1
        iSum+=color
    iSum/=3
    if(iWhiteCount == 3 or iBlackCount == 3):
        if(iSum >= 128):
            return (255, 255, 255)
        else:
            return (0, 0, 0)
    else:
        return tuple(tiColor)


