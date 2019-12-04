class Defuser:
    def __init__(self, serial, batteries, Abatteries = 0, Dbatteries = 0):
        self.serial = serial.upper()
        self.strikes = 0
        try:
            self.serialLastDigitOdd = int(self.serial[-1]]) // 2 == 1
        except:
            self.serialLastDigitOdd = false

        self.serialLastDigitEven = not self.serialLastDigitOdd

        self.serialContainsVowel = len([i for i in ['A', 'E', 'I', 'O', 'U'] if i in self.serial]) > 0
        self.batteries = batteries

    def wires(self, wireList):
        '''The wireList is a string of letters, R for red, B for Blue, Y for yellow, W for white, B for black'''
        wireList = wireList.upper()
        def getNumberOfColoredWires(color):
            return getNumberOfColoredWires(color)

        def getIndexOfLastColoredWire(color):
            return len(wireList) - wireList[::-1].index(color) - 1

        if len(wireList) == 3:
            #If there are no red wires, cut the second wire.
            if ('R' not in wireList):
                return 1
            elif (wireList[-1] == 'W'):
                return 2
            elif(getNumberOfColoredWires('B') >= 2):
                return getIndexOfLastColoredWire('B')
            else:
                return 2

        elif len(wireList) == 4:
            if self.serialLastDigitOdd and getNumberOfColoredWires('R') >= 2:
                return getIndexOfLastColoredWire('R')
            elif getNumberOfColoredWires('R') == 0 and wireList[-1] == 'Y':
                return 0
            elif getNumberOfColoredWires('B') == 1:
                return 0
            elif getNumberOfColoredWires('Y') > 1:
                return len(wireList - 1)
            else:
                return 1

        elif len(wireList) == 5:
            if self.serialLastDigitOdd and wireList[-1] == 'B':
                return 3
            elif getNumberOfColoredWires('R') == 1 and getNumberOfColoredWires('Y') > 1:
                return 0
            elif getNumberOfColoredWires('B') == 0:
                return 1
            else:
                return 0

        elif len(wireList) == 6:
            #If there are no yellow wires and the last digit of the serial number is odd, cut the third wire.
            if self.serialLastDigitOdd and getNumberOfColoredWires('Y') == 0:
                return 2

            #Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
            elif getNumberOfColoredWires('Y') == 1 and getNumberOfColoredWires('W') > 1:
                return 3

            #Otherwise, if there are no red wires, cut the last wire.
            elif getNumberOfColoredWires('R') == 0:
                return 5

            #Otherwse, cut the fourth wire.
            else:
                return 3
        else:
            #Raise Something
            pass

    def complicatedWires(self, wireCharacteristics=''):

        #Add these numbers with the characteristics to index into the array of options
        led = 8
        star = 4
        blue = 2
        red = 1

        whatToDo = ['C', 'S', 'S', 'S',
                    'C', 'C', 'D', 'P',
                    'D', 'B', 'P', 'S',
                    'B', 'B', 'P', 'D']

        wireValue = 0
        if 'R' in wireCharacteristics:
            wireValue += red
        if 'B' in wireCharacteristics:
            wireValue += blue
        if 'S' in wireCharacteristics:
            wireValue += star
        if 'L' in wireCharacteristics:
            wireValue += led




d = Defuser()
while(True):
    print(d.wires(input()))
