"""
Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Главное меню программы
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_implication.implication_solver import AbstractFuzzyImplicationSolver
from fuzzy_set import FuzzySet


class GodelImplicationSolver(AbstractFuzzyImplicationSolver):

    def solve(self, left_set: FuzzySet, right_set: FuzzySet) -> list[list[float]]:
        matrix = []

        for x in left_set.elements:
            row = []
            for y in right_set.elements:
                if left_set[x] <= right_set[y]:
                    row.append(1)
                else:
                    row.append(right_set[y])

            matrix.append(row)

        return matrix