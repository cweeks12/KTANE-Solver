from enum import Enum

class MorseFlash(Enum):
    DASH = auto()
    DOT = auto()

class Morse:
    characters = {
    (MorseFlash.DOT, MorseFlash.DASH): 'A',
    (MorseFlash.DASH, MorseFlash.DOT, MorseFlash.DOT, MorseFlash.DOT): 'B',
    (MorseFlash.DASH, MorseFlash.DOT, MorseFlash.DASH, MorseFlash.DOT): 'C',
    
    }
