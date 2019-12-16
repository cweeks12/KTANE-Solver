class SerialNumber:
    def __init__(self, serialNumber):
        if not (len(serialNumber) == 6):
            raise ValueError('Serial Number must be 6 digits long')
        self._serialNumber = serialNumber

    def __str__(self):
        return 'S/N: {}'.format(self._serialNumber)

    def __repr__(self):
        return 'SerialNumber: {}'.format(self._serialNumber)

    def getSerialNumber(self):
        return self._serialNumber

    def containsVowel(self):
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        for character in self._serialNumber:
            if character in VOWELS:
                return True
        return False

    def lastDigitOdd(self):
        try:
            lastDigitValue = int(self._serialNumber[-1])
        except ValueError:
            return False

        return lastDigitValue % 2 == 1

    def lastDigitEven(self):
        try:
            lastDigitValue = int(self._serialNumber[-1])
        except ValueError:
            return False

        return lastDigitValue % 2 == 0
