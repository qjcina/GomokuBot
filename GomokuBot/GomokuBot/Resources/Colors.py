from enum import Enum
class Colors(Enum):
    ButtonBorder = [143, 143, 143]
    EmptySeat = [238, 238, 238]
    NonEmptySeat = [255, 255, 255] #also Player2
    SeatHeader = [31, 41, 48]
    Player1 = [102, 102, 102]

def getColor(iColor):
    iColor = list(iColor)
    for oSingleColor in Colors:
        if(iColor==oSingleColor.value):
            return oSingleColor.name


