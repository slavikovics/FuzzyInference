class FuzzySet:
    def __init__(self, name, elements, degree_of_membership):
        self._name = name
        self._elements = elements
        self._degree_of_membership = degree_of_membership

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{set(zip(self._elements, self._degree_of_membership))}'

    def __eq__(self, other):
        ...

    def __contains__(self, item):
        ...

    def __len__(self):
        ...

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return set(zip(self._elements, self._degree_of_membership))
