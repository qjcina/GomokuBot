import threading
from Input.InputReader import InputReader
class CommandListener(object):
    def __init__(self):
        oListenerThread = threading.start_new_thread(target=self.listenerLoop)
        oListenerThread.start()
        self.oInput = InputReader()
        self.Flag = False
    def listenerLoop(self):
        while(True):
            self.oInput.waitForInput(32)
            self.Flag = ~self.Flag
            print("Mouse Flag is set to",self.Flag)
__oCommandListener = None
def getCommandListener():
    if(__oCommandListener is None):
        __oCommandListener = CommandListener()
    return __oCommandListener



