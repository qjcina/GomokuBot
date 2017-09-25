from enum import Enum
from Algorithm.MapGenerators.LineMapGenerator import LineMapGenerator
from Algorithm.MenuGenerators.BrightnessMapGenerator import BrightnessMapGenerator
class mapGenerator(Enum):
    DEFAULT = LineMapGenerator()
class menuGenerator(Enum):
    DEFAULT = BrightnessMapGenerator()
Settings= {
    "mapGenerator" : mapGenerator.DEFAULT,
    "menuGenerator" : menuGenerator.DEFAULT,
    "debugMode" : True
    }
