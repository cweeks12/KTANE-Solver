from Indicator import Indicator
from Battery import BatteryHolder, BatteryType
from SerialNumber import SerialNumber
from Port import Port, PortType

class Bomb:

    def __init__(self, serialNumber, modules=None, solved=None):
        self._serialNumber = SerialNumber(serialNumber)
        self._batteryHolders = []
        self._ports = []
        self._indicators = []
        self._modules = modules
        self._solved = solved
        if modules is not None and solved is not None:
            self._unsolved = self.modules - self._solved
        else:
            self._unsolved = None
        self._strikes = 0

    def addBatteryHolder(self, type, quantity):
        self._batteryHolders.append(BatteryHolder(type, quantity))

    def addPort(self, type):
        self._ports.append(Port(type))

    def addIndicator(self, lit, label):
        self._indicators.append(Indicator(lit, label))

    def setNumberOfModules(self, modules, solved=0):
        if modules < 1  or solved < 0:
            raise ValueError('Invalid number of modules.')

        self._modules = modules
        self._solved = solved
        self._unsolved = modules - solved

    def getNumberOfModules(self):
        return self._modules

    def getNumberOfSolvedModules(self):
        return self._solved

    def getNumberOfUnsolvedModules(self):
        return self._unsolved

    def getNumberOfStrikes(self):
        return self._strikes

    def getSerialNumber(self):
        return self._serialNumber.getSerialNumber()

    def incrementStrikes(self):
        self._strikes += 1

    def serialNumberContainsVowel(self):
        return self._serialNumber.containsVowel()

    def serialNumberLastDigitEven(self):
        return self._serialNumber.lastDigitEven()

    def serialNumberLastDigitOdd(self):
        return self._serialNumber.lastDigitOdd()

    def hasIndicator(self, indicator):
        for i in self._indicators:
            if i.getLabel() == indicator:
                return True
        return False

    def hasLitIndicator(self, indicator):
        for i in self._indicators:
            if i.getLabel() == indicator:
                return i.isLit()
        return False

    def hasPort(self, port):
        if not isinstance(port, PortType):
            raise ValueError('You must use the PortType enum in this function call')

        for p in self._ports:
            if p.getType() is port:
                return True
        return False

    def getNumberOfBatteries(self, type=None):
        if (not isinstance(type, BatteryType)) and (type is not None):
            raise ValueError('Use the BatteryType enum when selecting the type')

        numberOfBatteries = 0

        if type is not None:
            for holder in self._batteryHolders:
                if holder.getType() is type:
                    numberOfBatteries += holder.getQuantity()

        else:
            for holder in self._batteryHolders:
                numberOfBatteries += holder.getQuantity()

        return numberOfBatteries


if __name__ == '__main__':
    b = Bomb('ABC123')
    print(b.getSerialNumber())

    b.addPort(PortType.DVI_D)

    print(b.hasPort(PortType.DVI_D))
