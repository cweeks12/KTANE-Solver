try:
    #This Works when you call it from here as __main__
    from Helpers.Bomb.Bomb import Bomb
    from Helpers.Colors import Colors

except ModuleNotFoundError:
    #This is from context in the Defuser class
    from Modules.Helpers.Bomb.Bomb import Bomb
    from Modules.Helpers.Bomb.Port import PortType
    from Modules.Helpers.Colors import Colors

from enum import Enum, auto

class ComplicatedWires:

    CUT = 'Cut'
    DO_NOT_CUT = "Don't Cut"

    class Action(Enum):
        CUT = auto()
        DO_NOT_CUT = auto()
        EVEN_SERIAL = auto()
        PARALLEL = auto()
        BATTERIES = auto()

    def __init__(self, bomb):
        self._bomb = bomb

    def cutWire(self, wireCharacteristics):


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

        options = [ self.Action.CUT, self.Action.CUT, self.Action.DO_NOT_CUT, self.Action.BATTERIES,
                    self.Action.EVEN_SERIAL, self.Action.DO_NOT_CUT, self.Action.PARALLEL, self.Action.PARALLEL,
                    self.Action.EVEN_SERIAL, self.Action.CUT, self.Action.BATTERIES, self.Action.BATTERIES,
                    self.Action.EVEN_SERIAL, self.Action.PARALLEL, self.Action.EVEN_SERIAL, self.Action.DO_NOT_CUT]

        chosenOption = options[total]

        if chosenOption is self.Action.CUT:
            return True
        elif chosenOption is self.Action.DO_NOT_CUT:
            return False
        elif chosenOption is self.Action.BATTERIES:
            return self._bomb.getNumberOfBatteries() >= 2
        elif chosenOption is self.Action.EVEN_SERIAL:
            return self._bomb.serialNumberLastDigitEven()
        elif chosenOption is self.Action.PARALLEL:
            return self._bomb.hasPort(PortType.PARALLEL)

if __name__ == '__main__':
    cw = ComplicatedWires(None)
    print(cw.cutWire(''))
