from enum import Enum, auto

class Colors(Enum):
    RED = auto()
    BLUE = auto()
    WHITE = auto()
    YELLOW = auto()
    GREEN = auto()

    def stringToColor(colorString):
        colorString = colorString.upper()[0]

        colorLookupTable = {
        'B': Colors.BLUE,
        'G': Colors.GREEN,
        'R': Colors.RED,
        'W': Colors.WHITE,
        'Y': Colors.YELLOW
        }

        return colorLookupTable[colorString]
