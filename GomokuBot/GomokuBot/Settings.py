from enum import Enum
from .Algorithm.LineMapGenerator import LineMapGenerator
Settings= {
    "mapGenerator" : mapGenerator.DEFAULT,
    "lineDetector" : lineDetector.DEFAULT
    }
        
   


class mapGenerator(Enum):
    DEFAULT = LineMapGenerator()
class lineDetector(Enum):
    DEFAULT = 0