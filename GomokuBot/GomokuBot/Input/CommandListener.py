import threading
from Input.InputReader import InputReader
class CommandListener(object):
    def __init__(self):
        oListenerThread = threading.Thread(target=self.listenerLoop)
        
        self.oInput = InputReader()
        self.Flag = False
        oListenerThread.start()
    def listenerLoop(self):
        while(True):
            self.oInput.waitForInput(32)
            self.Flag = ~self.Flag
            print("Mouse Flag is set to",self.Flag)
__oCommandListener = None
def getCommandListener():
    global __oCommandListener
    if(__oCommandListener is None):
        __oCommandListener = CommandListener()
    return __oCommandListener




