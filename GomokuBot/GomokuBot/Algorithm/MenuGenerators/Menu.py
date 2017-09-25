class Menu(object):
    positions = {}
    def __init__(self, tiPlayer1Position, tiPlayer2Position, tiStartPosition, iLeftPlayerColor, iRightPlayerColor,  bIsRelative=False, oCoordinates=(0,0,0,0)):
        if(bIsRelative is True):
            tiPlayer1Position = list(tiPlayer1Position)
            tiPlayer2Position = list(tiPlayer2Position)
            tiStartPosition = list(tiStartPosition)
            iLeftPlayerColor = list(iLeftPlayerColor)
            iRightPlayerColor = list(iRightPlayerColor)
            tiPlayer1Position[0]+=oCoordinates[0]
            tiPlayer1Position[1]+=oCoordinates[1]
            tiPlayer2Position[0]+=oCoordinates[0]
            tiPlayer2Position[1]+=oCoordinates[1]
            tiStartPosition[0]+=oCoordinates[0]
            tiStartPosition[1]+=oCoordinates[1]
            iLeftPlayerColor[0]+=oCoordinates[0]
            iLeftPlayerColor[1]+=oCoordinates[1]
            iRightPlayerColor[0]+=oCoordinates[0]
            iRightPlayerColor[1]+=oCoordinates[1]
        self.positions["player1Position"] = tiPlayer1Position
        self.positions["player2Position"] = tiPlayer2Position
        self.positions["startPosition"] = tiStartPosition
        self.positions["player1Color"] = iLeftPlayerColor
        self.positions["player2Color"] = iRightPlayerColor
    def __getitem__(self, value):
        return self.positions[value]
