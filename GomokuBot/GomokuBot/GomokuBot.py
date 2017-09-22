from Input.WindowGrabber import WindowGrabber 
from Input.InputReader import InputReader
from ImageProcessing.ImagePreprocessor import ImagePreprocessor
from Algorithm.BotMain import BotMain
if __name__ == '__main__':
    print("GomokuBot 0.1a")
    image = WindowGrabber()
    (oImageEncoded, oCoordinates) = image.checkValid()
    oImagePreprocessor = ImagePreprocessor(oImageEncoded, oCoordinates)
    oProcessedImage = oImagePreprocessor.thresholding(oImagePreprocessor.getBitmap())
    oMainRobotLoop = BotMain(oProcessedImage, oCoordinates)
    oMainRobotLoop.process()