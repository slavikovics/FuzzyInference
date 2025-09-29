"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Треугольная норма min {{xi} ∪ {yi}}
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_conjunction import FuzzyConjunction
import unittest
from fuzzy_set import FuzzySet


class TestMinTNorm(unittest.TestCase):
    def test_example(self):
        # Данные из вашего примера
        A = FuzzySet('A',
            elements=['x1','x2','x3','x4'],
            degree_of_membership=[0.0, 0.1, 0.3, 1.0]
        )
        implication_matrix = [
            [1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 0.0, 0.0],
            [1.0, 1.0, 0.2, 0.0, 0.0],
            [1.0, 0.8, 0.2, 0.0, 0.0]
        ]

        expected_matrix = [
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.1, 0.1, 0.1, 0.0, 0.0],
            [0.3, 0.3, 0.2, 0.0, 0.0],
            [1.0, 0.8, 0.2, 0.0, 0.0]
        ]

        result = FuzzyConjunction.min(A, implication_matrix)
        self.assertEqual(result, expected_matrix)

        # Проверим sup по столбцам
        sup_result = [max(col) for col in zip(*result)]
        expected_sup = [1.0, 0.8, 0.2, 0.0, 0.0]
        self.assertEqual(sup_result, expected_sup)

    def test_all_ones(self):
        A = FuzzySet('A',
            elements=['x1','x2'],
            degree_of_membership=[1.0,1.0]
        )
        matrix = [
            [0.2,0.5],
            [0.7,0.9]
        ]
        expected = [
            [0.2,0.5],
            [0.7,0.9]
        ]
        result = FuzzyConjunction.min(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.7, 0.9])

    def test_all_zeros(self):
        A = FuzzySet('A',
            elements=['x1','x2'],
            degree_of_membership=[0.0,0.0]
        )
        matrix = [
            [0.2,0.5],
            [0.7,0.9]
        ]
        expected = [
            [0.0,0.0],
            [0.0,0.0]
        ]
        result = FuzzyConjunction.min(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.0, 0.0])

    def test_mixed_values(self):
        A = FuzzySet('A',
            elements=['x1','x2','x3'],
            degree_of_membership=[0.3,0.8,0.5]
        )
        matrix = [
            [0.6,0.2,0.9],
            [0.4,0.7,0.5],
            [0.9,0.1,0.3]
        ]
        expected = [
            [0.3,0.2,0.3],
            [0.4,0.7,0.5],
            [0.5,0.1,0.3]
        ]
        result = FuzzyConjunction.min(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.5,0.7,0.5])