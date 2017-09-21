from msvcrt import getch
class InputReader(object):
	def waitForInput(self, iKeyCode):
		while(True):
			iReadKey = ord(getch())
			if(iReadKey == iKeyCode):
				break
			pass
	def waitForAnyInput(self):
		iReadKey = ord(getch())
		return iReadKey

