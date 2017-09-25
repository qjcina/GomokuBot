from win32 import win32api
import win32con
import time
from Input.CommandListener import *
class MouseClicker(object):
    lastMousePosition = None
    def __init__(self):
        self.oCommandListener = getCommandListener()
        self.lastPos = (0,0)
    def click(self, iX, iY):
        if(self.oCommandListener.Flag is False):
            flags, hcursor, (x, y) = win32gui.GetCursorInfo()
            if(self.lastPos != (x, y)):
                print("If you want to block mouse moving press SPACE!")
            self.lastPos = (x, y)
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
            print("Mouse click at",x,y)
            return True
        else:
            print("Tried to click at",x,y)
            return False
    def tryClick(self, iX, iY, iTimeToSleep=1):
        while(not self.click(iX, iY)):
            time.sleep(iTimeToSleep)
            pass




