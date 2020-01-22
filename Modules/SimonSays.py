try:
    #This Works when you call it from here as __main__
    from Helpers.Bomb.Bomb import Bomb
    from Helpers.Colors import Colors

except ModuleNotFoundError:
    #This is from context in the Defuser class
    from Modules.Helpers.Bomb.Bomb import Bomb
    from Modules.Helpers.Bomb.Port import PortType
    from Modules.Helpers.Colors import Colors

class SimonSays:

    def __init__(self, bomb):
        self._bomb = bomb

    def solve(self, flashes):
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

        if self._bomb.serialNumberContainsVowel():
            selectedDictionary = vowelTranslations
        else:
            selectedDictionary = noVowelTranslation

        pressesToReturn = []
        for flash in flashes:
            pressesToReturn.append(selectedDictionary[flash][self._bomb.getNumberOfStrikes()])

        return pressesToReturn
