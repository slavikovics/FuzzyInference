class FuzzySet:
    def __init__(self, name, elements, degree_of_membership):
        self._name = name
        self._elements = elements
        self._degree_of_membership = degree_of_membership

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self._name} = {set(zip(self._elements, self._degree_of_membership))}'

    def __eq__(self, other):
        return self._name == other.name and self.items == other.items

    def __contains__(self, item):
        return item in self._elements

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, item):
        for (element, degree) in zip(self._elements, self._degree_of_membership):
            if element == item:
                return degree

        raise KeyError(f'Element with name "{item}" was not found.')

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return set(zip(self._elements, self._degree_of_membership))

    @property
    def elements(self):
        return self._elements
