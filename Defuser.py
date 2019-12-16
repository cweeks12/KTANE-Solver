from Modules.Helpers.Bomb.Bomb import Bomb
from Modules.Helpers.Colors import Colors

import Modules.TheButton

class Defuser:
    def __init__(self, serialNumber):
        self.bomb = Bomb(serialNumber)



    def complicatedWires(self, wireCharacteristics=''):

        class Action(Enum):
            CUT = auto()
            DO_NOT_CUT = auto()
            EVEN_SERIAL = auto()
            PARALLEL = auto()
            BATTERIES = auto()

        total = 0

        #Add these numbers with the characteristics to index into the array of options
        star = 1
        led = 2
        blue = 4
        red = 8

        wireCharacteristics = wireCharacteristics.upper()
        if 'S' in wireCharacteristics:
            total += star
        if 'L' in wireCharacteristics:
            total += led
        if 'B' in wireCharacteristics:
            total += blue
        if 'R' in wireCharacteristics:
            total += red

        options = [ Action.CUT, Action.CUT, Action.DO_NOT_CUT, Action.BATTERIES,
                    Action.EVEN_SERIAL, Action.DO_NOT_CUT, Action.PARALLEL, Action.PARALLEL,
                    Action.EVEN_SERIAL, Action.CUT, Action.BATTERIES, Action.BATTERIES,
                    Action.EVEN_SERIAL, Action.PARALLEL, Action.EVEN_SERIAL, Action.DO_NOT_CUT]

        chosenOption = options[total]

        if chosenOption is Action.CUT:
            return True
        elif chosenOption is Action.DO_NOT_CUT:
            return False
        elif chosenOption is Action.BATTERIES:
            return bomb.getNumberOfBatteries() >= 2
        elif chosenOption is Action.EVEN_SERIAL:
            return bomb.serialNumberLastDigitEven()
        elif chosenOption is Action.PARALLEL:
            return bomb.hasPort(PortType.PARALLEL)


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
