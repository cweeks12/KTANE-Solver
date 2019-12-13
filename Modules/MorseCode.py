from Helpers.Morse import Morse

class MorseCode:
    def __init__(self):
        self.frequencies = {
            'shell': '3.505 MHz',
            'halls': '3.515 MHz',
            'slick': '3.522 MHz',
            'trick': '3.532 MHz',
            'boxes': '3.535 MHz',
            'leaks': '3.542 MHz',
            'strobe': '3.545 MHz',
            'bistro': '3.552 MHz',
            'flick': '3.555 MHz',
            'bombs': '3.565 MHz',
            'break': '3.572 MHz',
            'brick': '3.575 MHz',
            'steak': '3.582 MHz',
            'sting': '3.592 MHz',
            'vector': '3.595 MHz',
            'beats': '3.600 MHz'
        }

        self.lettersInWord = []
        self.possibilities = self.frequencies.keys()


    def addLetter(self, letterInMorse):
        self.lettersInWord.append(Morse.morseToWord(letterInMorse, uppercase=False))
        self.calculatePossibleWords()

    def calculatePossibleWords(self):
        if self.lettersInWord == []:
            return self.frequencies.keys()

        self.possibilities = []

        for key in self.frequencies.keys():
            if all(letter in key for letter in self.lettersInWord):
                self.possibilities.append(key)

    def getNumberOfPossibilities(self):
        return len(self.possibilities)

    def getPossibilities(self):
        return self.possibilities

    def frequencyFromWord(self, word):
        return self.frequencies[word.lower()]

    def frequencyFromMorseWord(self, morseWord):
        return self.frequencies[Morse.morseToWord(morseWord, uppercase=False)]

    def getAnswer(self):
        if len(self.possibilities) > 1:
            return ''
        else:
            return self.frequencyFromWord(self.possibilities[0])

    def reset(self):
        self.lettersInWord = []
        self.possibilities = self.frequencies.keys()


if __name__ == '__main__':
    mc = MorseCode()

    while mc.getNumberOfPossibilities() > 1:
        mc.addLetter(input())
        print(mc.lettersInWord)
        print(mc.getNumberOfPossibilities())
        print(mc.getPossibilities())

    print(mc.getAnswer())
