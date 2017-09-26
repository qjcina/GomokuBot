class MapElement(object):
    def __init__(self, iXPosition, iYPosition):
        self.iXPosition = iXPosition
        self.iYPosition = iYPosition
        self.iPlayerToken = 0
    def getValue(self):
        return (self.iXPosition, self.iYPosition)

