"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Класс для представления нечеткого множества
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import math


class FuzzySet:
    def __init__(self, name, elements, degree_of_membership):
        if len(elements) != len(degree_of_membership):
            raise ValueError("Elements and membership degrees must be the same length.")

        self._name = name
        self._data = dict(zip(elements, degree_of_membership))

    def __str__(self):
        result = ''
        for key, value in self._data.items():
            cortege = f'<{key}, {value}>'
            if result != '':
                result = result + ', ' + cortege

            else:
                result = result + cortege

        return self.name + ' = {' + result + '}'

    def __repr__(self):
        return f'{self._name} = {self._data}'

    def __eq__(self, other):
        if not isinstance(other, FuzzySet):
            return NotImplemented

        if self._data.keys() != other._data.keys():
            return False

        for key in self._data:
            if not math.isclose(
                self._data[key],
                other._data[key],
                rel_tol=1e-9,
                abs_tol=1e-12
            ):
                return False

        return True

    def __contains__(self, item):
        return item in self._data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        if item not in self._data:
            raise KeyError(f'Element "{item}" not found.')
        return self._data[item]

    def is_like(self, other):
        return self._data.keys() == other._data.keys()

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return set(self._data.items())

    @property
    def degrees_of_membership(self):
        return list(self._data.values())

    @property
    def elements(self):
        return list(self._data.keys())
