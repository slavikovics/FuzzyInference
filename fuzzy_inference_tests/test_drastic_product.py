"""
Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Тесты для драстического произведения
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_set import FuzzySet
from fuzzy_conjunction import FuzzyConjunction
import unittest


class TestDrasticProduct(unittest.TestCase):
    def test_example_basic(self):
        A = FuzzySet('A', elements=['x1','x2'], degree_of_membership=[0.5,1.0])
        matrix = [
            [0.7, 1.0],
            [0.2, 0.8]
        ]

        expected = [
            [0.0, 0.5],
            [0.2, 0.8]
        ]
        result = FuzzyConjunction.drastic_product(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.2, 0.8])

    def test_all_ones(self):
        A = FuzzySet('A', elements=['x1','x2'], degree_of_membership=[1.0,1.0])
        matrix = [
            [0.4,0.6],
            [0.7,0.9]
        ]
        expected = [
            [0.4,0.6],
            [0.7,0.9]
        ]
        result = FuzzyConjunction.drastic_product(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.7,0.9])

    def test_all_below_one(self):
        A = FuzzySet('A', elements=['x1','x2'], degree_of_membership=[0.2,0.5])
        matrix = [
            [0.3,0.6],
            [0.4,0.8]
        ]
        expected = [
            [0.0,0.0],
            [0.0,0.0]
        ]
        result = FuzzyConjunction.drastic_product(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.0,0.0])

    def test_mixed_values(self):
        A = FuzzySet('A', elements=['x1','x2','x3'], degree_of_membership=[0.0,1.0,0.6])
        matrix = [
            [0.9,0.0,1.0],
            [0.2,1.0,0.5],
            [1.0,0.4,0.3]
        ]

        expected = [
            [0.0,0.0,0.0],
            [0.2,1.0,0.5],
            [0.6,0.0,0.0]
        ]
        result = FuzzyConjunction.drastic_product(A, matrix)
        self.assertEqual(result, expected)
        sup_result = [max(col) for col in zip(*result)]
        self.assertEqual(sup_result, [0.6,1.0,0.5])