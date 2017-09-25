class Menu(object):
    positions = {}
    def __init__(self, tiPlayer1Position, tiPlayer2Position, tiStartPosition, bIsRelative):
        self.positions["player1Position"] = tiPlayer1Position
        self.positions["player2Position"] = tiPlayer2Position
        self.positions["startPosition"] = tiStartPosition
    def __getitem__(self, value):
        return self.positions[value]
