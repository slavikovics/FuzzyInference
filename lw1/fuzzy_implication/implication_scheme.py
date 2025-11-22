"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Класс для хранения записей о нечеткой импликации
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from typing import Optional

from fuzzy_set import FuzzySet

class ImplicationScheme:
    def __init__(self, first, second):
        self._first = first
        self._second = second
        self.applied_sets = []
        self.first_set: Optional[FuzzySet] = None
        self.second_set: Optional[FuzzySet] = None
        self.solution = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self._first} ~> {self._second}'

    def __eq__(self, other):
        return self._first == other.first and self._second == other.second

    def str_with_solution(self):
        if self.solution is None or len(self.solution) == 0:
            return str(self)

        result = str(self) + '\n'

        all_values = self.first_set.elements + self.second_set.elements + [el for row in self.solution for el in row]

        if len(all_values) == 0:
            return str(self)

        col_width = max(len(f"{v}") for v in all_values) + 1

        result += ' ' * col_width

        for i in self.second_set.elements:
            result += f'{i:{col_width}}'
        result += '\n'

        for row_name, row in zip(self.first_set.elements, self.solution):
            result += f"{row_name:{col_width}}"
            for el in row:
                result += f"{str(el):{col_width}}"
            result += '\n'

        return result

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second