from enum import Enum
from Algorithm.MapGenerators.LineMapGenerator import LineMapGenerator
from Algorithm.MenuGenerators.BrightnessMapGenerator import BrightnessMapGenerator
from Algorithm.BotLogics.Simple.ZeroDepth import ZeroDepth
class mapGenerator(Enum):
    DEFAULT = LineMapGenerator()
class menuGenerator(Enum):
    DEFAULT = BrightnessMapGenerator()
class botLogics(Enum):
    DEFAULT = ZeroDepth()
Settings = {
    "mapGenerator" : mapGenerator.DEFAULT,
    "menuGenerator" : menuGenerator.DEFAULT,
    "botLogics": botLogics.DEFAULT,
    "debugMode" : True
    }
