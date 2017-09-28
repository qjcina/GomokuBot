import matplotlib.pyplot as plot
import pyscreenshot as ImageGrab
__global_oHeuristicMap = None
__global_oCoorinates = None
__global_bPrint = False
def saveHeuristicMap(oHeurMap, oRawMap):
    global __global_oHeuristicMap
    if(__global_oHeuristicMap==None):
        __global_oHeuristicMap = [[None for x in range(0,len(oRawMap[0]))] for y in range(0,len(oRawMap))]
    for y in range(0,len(oRawMap)):
        for x in range(0,len(oRawMap[0])):
            __global_oHeuristicMap[y][x] = (oHeurMap[y][x], oRawMap[y][x])

def saveWindow(oCoordinates):
    global __global_oCoorinates
    __global_oCoorinates = oCoordinates

def setForPrinting():
    global __global_bPrint
    __global_bPrint = True
def printHeuristicMap():
    global __global_bPrint
    if(__global_bPrint==True):
        global __global_oHeuristicMap
        global __global_oCoorinates
        if(__global_oHeuristicMap!=None):
            image = ImageGrab.grab(bbox=__global_oCoorinates)
            plot.imshow(image, cmap='gray')
            for row in __global_oHeuristicMap:
                for element in row:
                    x = element[1][0] - __global_oCoorinates[0]
                    y = element[1][1] - __global_oCoorinates[1]
                    plot.scatter(x, y)
                    plot.annotate(str(element[0]), xy=(x, y), xytext=(x, y+5), arrowprops=dict(facecolor='black',shrink=0.05))
            plot.show()
            __global_bPrint=False