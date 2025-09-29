"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Импликация Вебера
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import unittest
from fuzzy_implication import WeberImplicationSolver
from parser import parse_fuzzy_set


class TestWeberImplicationSolver(unittest.TestCase):

    def setUp(self):
        self.solver = WeberImplicationSolver()

    def test_basic_implication(self):
        left_set = parse_fuzzy_set('A = {<x1, 0.8>, <x2, 0.5>}')
        right_set = parse_fuzzy_set('B = {<y1, 0.9>, <y2, 0.3>}')

        result = self.solver.solve(left_set, right_set)

        expected = [
            [1.0, 1.0],
            [1.0, 1.0]
        ]

        self.assertEqual(result, expected)

    def test_absolute_truth_premise(self):
        left_set = parse_fuzzy_set('A = {<x1, 1.0>, <x2, 1.0>}')
        right_set = parse_fuzzy_set('B = {<y1, 0.7>, <y2, 0.2>, <y3, 1.0>}')

        result = self.solver.solve(left_set, right_set)

        expected = [
            [0.7, 0.2, 1.0],
            [0.7, 0.2, 1.0]
        ]

        self.assertEqual(result, expected)

    def test_mixed_premises(self):
        left_set = parse_fuzzy_set('A = {<x1, 0.9>, <x2, 1.0>, <x3, 0.0>}')
        right_set = parse_fuzzy_set('B = {<y1, 0.5>}')

        result = self.solver.solve(left_set, right_set)

        expected = [
            [1.0],
            [0.5],
            [1.0]
        ]

        self.assertEqual(result, expected)

    def test_edge_cases(self):
        left_set = parse_fuzzy_set('A = {<x1, 0.999>, <x2, 1.0>}')
        right_set = parse_fuzzy_set('B = {<y1, 0.0>, <y2, 1.0>}')

        result = self.solver.solve(left_set, right_set)

        expected = [
            [1.0, 1.0],
            [0.0, 1.0]
        ]

        self.assertEqual(result, expected)

    def test_single_element_sets(self):
        left_set = parse_fuzzy_set('A = {<x1, 1.0>}')
        right_set = parse_fuzzy_set('B = {<y, 0.3>}')

        result = self.solver.solve(left_set, right_set)

        expected = [[0.3]]
        self.assertEqual(result, expected)

    def test_empty_sets(self):
        left_set = parse_fuzzy_set('A = {}')
        right_set = parse_fuzzy_set('B = {<y1, 0.5>, <y2, 0.8>}')

        result = self.solver.solve(left_set, right_set)

        expected = []
        self.assertEqual(result, expected)

        left_set = parse_fuzzy_set('A = {<x1, 0.5>, <x2, 1.0>}')
        right_set = parse_fuzzy_set('A = {}')

        result = self.solver.solve(left_set, right_set)

        expected = [[], []]
        self.assertEqual(result, expected)