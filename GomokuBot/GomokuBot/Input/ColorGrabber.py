import pyscreenshot as ImageGrab

def getPixelColor(i_x, i_y, bIsRelative=False, oCoordinates=(0,0,0,0)):
    if(bIsRelative is True):
        i_x += oCoordinates[0]
        i_y += oCoordinates[1]
    return ImageGrab.grab().load()[i_x, i_y]




