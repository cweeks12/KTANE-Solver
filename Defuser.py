from Modules.Helpers.Bomb.Bomb import Bomb
from Modules.Helpers.Colors import Colors
from Modules.Helpers.Bomb.Battery import BatteryHolder, BatteryType
from Modules.Helpers.Bomb.Indicator import Indicator
from Modules.Helpers.Bomb.Port import Port, PortType

import Modules.TheButton

class Defuser:
    def __init__(self, serialNumber, modules, batteryHolders=None, indicators=None, ports=None):
        self.bomb = Bomb(serialNumber, batteryHolders, indicators, ports, modules)

    def getBomb(self):
        return self.bomb

if __name__ == '__main__':
    d = Defuser('123ABC', 5)
