from Modules.Helpers.Bomb.Bomb import Bomb
from Modules.Helpers.Colors import Colors

import Modules.TheButton

class Defuser:
    def __init__(self, serialNumber):
        self.bomb = Bomb(serialNumber)

    def simonSays(self, flashes):
        if not isinstance(flashes, list):
            raise ValueError('Need a list')
        for flash in flashes:
            if not isinstance(flash, Colors):
                raise ValueError('Need Colors')

        vowelTranslations = {Colors.RED: [Colors.BLUE, Colors.YELLOW, Colors.GREEN],
                        Colors.BLUE: [Colors.RED, Colors.GREEN, Colors.RED],
                        Colors.GREEN: [Colors.YELLOW, Colors.BLUE, Colors.YELLOW],
                        Colors.YELLOW: [Colors.GREEN, Colors.RED, Colors.BLUE]}

        noVowelTranslation = {Colors.RED: [Colors.BLUE, Colors.RED, Colors.YELLOW],
                        Colors.BLUE: [Colors.YELLOW, Colors.BLUE, Colors.GREEN],
                        Colors.GREEN: [Colors.GREEN, Colors.YELLOW, Colors.BLUE],
                        Colors.YELLOW: [Colors.RED, Colors.GREEN, Colors.RED]}

        if bomb.serialNumberContainsVowel():
            selectedDictionary = vowelTranslations
        else:
            selectedDictionary = noVowelTranslation

        pressesToReturn = []
        for flash in flashes:
            pressesToReturn.append(selectedDictionary[flash][bomb.getNumberOfStrikes()])

        return pressesToReturn

if __name__ == '__main__':
    d = Defuser('123ABC')
