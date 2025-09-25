class FuzzyImplication:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self._first} ~> {self._second}'

    def __eq__(self, other):
        return self._first == other.first and self._second == other.second

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second