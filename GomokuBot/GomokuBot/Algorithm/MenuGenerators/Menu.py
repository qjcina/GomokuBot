class Menu(object):
    positions = {}
    def __init__(self, tiPlayer1Position, tiPlayer2Position, tiStartPosition, bIsRelative=False, oCoordinates=(0,0,0,0)):
        if(bIsRelative is True):
            tiPlayer1Position[0]+=oCoordinates[0]
            tiPlayer1Position[1]+=oCoordinates[1]
            tiPlayer2Position[0]+=oCoordinates[0]
            tiPlayer2Position[1]+=oCoordinates[1]
            tiStartPosition[0]+=oCoordinates[0]
            tiStartPosition[1]+=oCoordinates[1]
        self.positions["player1Position"] = tiPlayer1Position
        self.positions["player2Position"] = tiPlayer2Position
        self.positions["startPosition"] = tiStartPosition
    def __getitem__(self, value):
        return self.positions[value]
