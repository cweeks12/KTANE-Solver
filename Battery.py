from enum import Enum, auto

class BatteryType(Enum):
    AA = auto()
    D = auto()

class BatteryHolder:
    def __init__(self, type, quantity):
        if not isinstance(type, BatteryType):
            raise ValueError('You must select an enumerated type from the BatteryType class for the battery type.')
        self._type = type

        if quantity <= 0:
            raise ValueError('Quantity of batteries must be positive.')
        self._quantity = quantity

    def getType(self):
        return self._type

    def getQuantity(self):
        return self._quantity
