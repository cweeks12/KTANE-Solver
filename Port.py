from enum import Enum, auto

class PortType(Enum):
    DVI_D = auto()
    PARALLEL = auto()
    PS_2 = auto()
    RJ_45 = auto()
    SERIAL = auto()
    STEREO_RCA = auto()

class Port:
    def __init__(self, type):
        if not isinstance(type, PortType):
            raise ValueError('You must select a port type from the PortType class')
        self._type = type

    def getType(self):
        return self._type
