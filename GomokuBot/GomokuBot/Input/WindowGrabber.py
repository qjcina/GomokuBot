import pyscreenshot as ImageGrab
import matplotlib.pyplot as plot
import matplotlib.image as img
from Resources.DebugMemory import saveWindow
import numpy as numpy
from win32 import win32gui
from multiprocessing import Process
from Input.InputReader import InputReader
"""
WindowGrabber class catches user selected rectangle on the screen
and makes region screenshot. 
"""
class WindowGrabber(object):
    figure = None
    def __grabImage(self):
        self.image = ImageGrab.grab(bbox=self.coordinates)
        saveWindow(self.coordinates)
    """
    checkValid method lets user decide if image is valid.
    Returns image and its coordinates.
    """
    def checkValid(self):
        self.drawImage()
        oInput = InputReader()
        while(True):
            print("Press X to discard image, press C to continue")
            iReadKey = oInput.waitForAnyInput()
            if(iReadKey == 99):
                break
            if(iReadKey == 120):
                plot.close(self.figure)
                self.coordinates = self.markCoords()
                self.__grabImage()
                self.drawImage()
        plot.close(self.figure)
        return (self.image, self.coordinates)

    def drawImage(self):
        self.figure = plot.figure()
        image = self.image.convert('L')
        plot.imshow(image, cmap='gray')
        plot.show(block=False)

    def markCoords(self):
        oInput = InputReader()
        print("Mark top-left point: K")
        oInput.waitForInput(107)
        flags, hcursor, (left, top) = win32gui.GetCursorInfo()
        print("Top-left corner marked at:", left, top)
        print("Mark bottom-right point: K")
        oInput.waitForInput(107)
        flags, hcursor, (right, bottom) = win32gui.GetCursorInfo()
        print("Bottom-right corner marked at:", right, bottom)
        return (left, top, right, bottom)

    def __init__(self):
        self.coordinates = self.markCoords()
        self.__grabImage()