import cv2
from Resources.Settings import Settings
class BotMain(object):
    def __init__(self, oBitmap, oCoordinates):
        self.oBitmap = oBitmap
        self.oCoordinates = oCoordinates
        self.isReadyToExit = False

    def process(self):
        oMapGenerator = Settings["mapGenerator"].value
        oMapGenerator.createMap(self.oBitmap)
        while(True):

            if(self.isReadyToExit):
                break


