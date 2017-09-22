from enum import Enum
from Algorithm.MapGenerators.LineMapGenerator import LineMapGenerator
class mapGenerator(Enum):
    DEFAULT = LineMapGenerator()
Settings= {
    "mapGenerator" : mapGenerator.DEFAULT,
    "debugMode" : True
    }
