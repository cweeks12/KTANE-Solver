class Indicator:
    def __init__(self, lit, tag):
        if len(tag) != 3:
            raise ValueError('Tags must be three characters long')
        self._tag = tag
        self._lit = lit

    def isLit(self):
        return self._lit

    def getLabel(self):
        return self._tag
