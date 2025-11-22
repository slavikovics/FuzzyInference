"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Нечёткая конъюнкция
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_set import FuzzySet
from fuzzy_implication import ImplicationScheme


class FuzzyConjunction:

    @staticmethod
    def min(left_set :FuzzySet, implication_matrix :list[list[float]]) -> list[list[float]]:
        if len(left_set.elements) != len(implication_matrix):
            raise Exception(f'Set and matrix are incompatible.')

        result = []

        for x in range(len(left_set.elements)):
            row = []
            for y in range(len(implication_matrix[x])):
                row.append(min(left_set.degrees_of_membership[x], implication_matrix[x][y]))

            result.append(row)

        return result

    @staticmethod
    def drastic_product(left_set :FuzzySet, implication_scheme :ImplicationScheme) -> list[list[float]]:
        implication_matrix = implication_scheme.solution

        if len(left_set.elements) != len(implication_matrix):
            raise Exception(f'Set and matrix are incompatible.')

        result = []

        for index, x in implication_scheme.first_set.get_set_order().items():
            row = []
            for y in range(len(implication_matrix[index])):
                if max(left_set[x], implication_matrix[index][y]) == 1:
                    row.append(min(left_set[x], implication_matrix[index][y]))
                else:
                    row.append(0)

            result.append(row)

        return result