"""
Лабораторная работа 3 по дисциплине ЛОИС

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

from fuzzy_set import FuzzySet


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
    def drastic_product(left_set :FuzzySet, implication_matrix :list[list[float]]) -> list[list[float]]:
        if len(left_set.elements) != len(implication_matrix):
            raise Exception(f'Set and matrix are incompatible.')

        result = []

        for x in range(len(left_set.elements)):
            row = []
            for y in range(len(implication_matrix[x])):
                if max(left_set.degrees_of_membership[x], implication_matrix[x][y]) == 1:
                    row.append(min(left_set.degrees_of_membership[x], implication_matrix[x][y]))
                else:
                    row.append(0)

            result.append(row)

        return result