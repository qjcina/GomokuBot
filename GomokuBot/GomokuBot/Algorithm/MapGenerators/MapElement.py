class MapElement(object):
    def __init__(self, iXPosition, iYPosition):
        self.iXPosition = iXPosition
        self.iYPosition = iYPosition
    def getValue(self):
        return (self.iXPosition, self.iYPosition)

