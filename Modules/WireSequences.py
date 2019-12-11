from Colors import Colors

class WireSequences:

    def __init__(self):
        self._wireSequences = { Colors.RED: ['C', 'B', 'A', 'AC', 'B', 'AC', 'ABC', 'AB', 'B'],
                                Colors.BLUE: ['B', 'AC', 'B', 'A', 'B', 'BC', 'C', 'AC', 'A'],
                                Colors.BLACK: ['ABC', 'AC', 'B', 'AC', 'B', 'BC', 'AB', 'C', 'C'] }
        self._wireCounts = { Colors.RED: 0,
                                Colors.BLUE: 0,
                                Colors.BLACK: 0 }

    def reset(self):
        self._wireCounts = { Colors.RED: 0,
                                Colors.BLUE: 0,
                                Colors.BLACK: 0 }

    def _colorToString(self, color):
        return self._wireSequences[color][self._wireCounts[color]]

    def shouldICut(self, color, terminal=None):
        connectionsToCut = self._colorToString(color)
        self._wireCounts[color] += 1

        if terminal is not None:
            return terminal[0].upper() in connectionsToCut
        else:
            return connectionsToCut
