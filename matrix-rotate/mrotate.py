from functools import partial
from math import log10

class Field:
    def __init__(self, m, n):
        self._m = m
        self._n = n
        self._field = self._generate()

    def _generate(self):
        g = iter(range(1, self._m * self._n + 1))
        return [[next(g) for x in range(self._m)] for y in range(self._n)]

    def show(self):
        fmt_length = int(log10(self._m * self._n)) + 1
        fmt = ("{:" + str(fmt_length) + "}").format
        for row in self._field:
            print(' '.join(map(fmt, row)))

def main():
    field = Field(10, 10)
    field.show()

if __name__ == '__main__':
    main()
