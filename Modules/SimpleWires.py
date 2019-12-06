class SimpleWires:
    def solve(self, wireString):
        '''The wireList is a string of letters, R for red, B for Blue, Y for yellow, W for white, B for black'''
        def getNumberOfColoredWires(color):
            return wireList.count(color)

        def getIndexOfLastColoredWire(color):
            return len(wireList) - wireList[::-1].index(color) - 1

        wireList = [Colors.stringToColor(wire) for wire in wireString.upper()]

        if len(wireList) == 3:
            #If there are no red wires, cut the second wire.
            if (Colors.RED not in wireList):
                return 1
            elif (wireList[-1] == Colors.WHITE):
                return 2
            elif(getNumberOfColoredWires(Colors.BLUE) >= 2):
                return getIndexOfLastColoredWire(Colors.BLUE)
            else:
                return 2

        elif len(wireList) == 4:
            if self.bomb.serialNumberLastDigitOdd() and getNumberOfColoredWires(Colors.RED) >= 2:
                return getIndexOfLastColoredWire(Colors.RED)
            elif getNumberOfColoredWires(Colors.RED) == 0 and wireList[-1] == Colors.YELLOW:
                return 0
            elif getNumberOfColoredWires(Colors.BLUE) == 1:
                return 0
            elif getNumberOfColoredWires(Colors.YELLOW) > 1:
                return len(wireList - 1)
            else:
                return 1

        elif len(wireList) == 5:
            if self.bomb.serialNumberLastDigitOdd() and wireList[-1] == Colors.BLUE:
                return 3
            elif getNumberOfColoredWires(Colors.RED) == 1 and getNumberOfColoredWires(Colors.YELLOW) > 1:
                return 0
            elif getNumberOfColoredWires(Colors.BLUE) == 0:
                return 1
            else:
                return 0

        elif len(wireList) == 6:
            #If there are no yellow wires and the last digit of the serial number is odd, cut the third wire.
            if self.bomb.serialNumberLastDigitOdd() and getNumberOfColoredWires(Colors.YELLOW) == 0:
                return 2

            #Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
            elif getNumberOfColoredWires(Colors.YELLOW) == 1 and getNumberOfColoredWires(Colors.WHITE) > 1:
                return 3

            #Otherwise, if there are no red wires, cut the last wire.
            elif getNumberOfColoredWires(Colors.RED) == 0:
                return 5

            #Otherwse, cut the fourth wire.
            else:
                return 3
        else:
            #Raise Something
            pass
