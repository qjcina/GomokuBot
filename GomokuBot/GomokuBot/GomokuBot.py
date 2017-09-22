from WindowGrabber import WindowGrabber
from InputReader import InputReader
from ImagePreprocessor import ImagePreprocessor
if __name__ == '__main__':
    print("GomokuBot 0.1a")
    image = WindowGrabber()
    (oImageEncoded, oCoordinates) = image.checkValid()
    oImagePreprocessor = ImagePreprocessor(oImageEncoded, oCoordinates)