try:
    #This Works when you call it from here as __main__
    from Helpers.Bomb.Bomb import Bomb
    from Helpers.Bomb.Indicator import Indicator
    from Helpers.Bomb.Battery import BatteryType
    from Helpers.Colors import Colors
except ModuleNotFoundError:
    from Modules.Helpers.Bomb.Bomb import Bomb
    from Modules.Helpers.Bomb.Indicator import Indicator
    from Modules.Helpers.Colors import Colors

class TheButton:

    ACTION_HOLD = 'Hold'
    ACTION_PRESS_AND_RELEASE = 'Press and Release'

    def __init__(self, color, text, bomb):

        self._text = text.upper()
        self._color = color
        self._bomb = bomb

    def holdOrPress(self):
        if self._color == Colors.BLUE and self._text == 'ABORT':
            return self.ACTION_HOLD
        elif self._bomb.getNumberOfBatteries() > 1 and self._text == 'DETONATE':
            return self.ACTION_PRESS_AND_RELEASE
        elif self._color == Colors.WHITE and self._bomb.hasLitIndicator('CAR'):
            return self.ACTION_HOLD
        elif self._bomb.getNumberOfBatteries() > 2 and self._bomb.hasLitIndicator('FRK'):
            return self.ACTION_PRESS_AND_RELEASE
        elif self._color == Colors.YELLOW:
            return self.ACTION_HOLD
        elif self._color == Colors.RED and self._text == 'HOLD':
            return self.ACTION_PRESS_AND_RELEASE
        else:
            return self.ACTION_HOLD

    def releaseTime(self, stripColor):
        if stripColor == Colors.BLUE:
            return '4'
        elif stripColor == Colors.WHITE:
            return '1'
        elif stripColor == Colors.YELLOW:
            return '5'
        else:
            return '1'



if __name__ == '__main__':
    b = TheButton(Colors.RED, 'abort', Bomb('123ABC').addIndicator('FRK', True).addBatteryHolder(BatteryType.AA, 3))
    print(b.holdOrPress())
