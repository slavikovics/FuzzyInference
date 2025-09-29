"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Тесты для парсера нечёткого множества
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import unittest
from parser import parse_fuzzy_set


class FuzzySetParserTests(unittest.TestCase):

    def test_names_parsing(self):
        set_str = 'A = {}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'A')

        set_str = 'B = {}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'B')

        set_str = 'C = {}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'C')

    def test_only_correct_names_allowed(self):
        set_str = 'Set = {}'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_set(set_str)

        set_str = 'set = {}'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_set(set_str)

        set_str = 's = {}'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_set(set_str)

        set_str = '_ = {}'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_set(set_str)

    def test_single_element_parsing(self):
        set_str = 'A = {<x1, 0.5>}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'A')
        self.assertEqual(len(fuzzy_set.elements), 1)
        self.assertEqual(fuzzy_set['x1'], 0.5)

    def test_multiple_elements_parsing(self):
        set_str = 'A = {<x1, 0.0>, <x2, 1.0>, <x3, 0.7>}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'A')
        self.assertEqual(len(fuzzy_set.elements), 3)
        self.assertEqual(fuzzy_set['x1'], 0.0)
        self.assertEqual(fuzzy_set['x2'], 1.0)
        self.assertEqual(fuzzy_set['x3'], 0.7)

    def test_different_element_names(self):
        set_str = 'B = {<cat1, 0.0>, <cat2, 0.5>, <dog, 0.8>}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'B')
        self.assertEqual(len(fuzzy_set.elements), 3)
        self.assertEqual(fuzzy_set['cat1'], 0.0)
        self.assertEqual(fuzzy_set['cat2'], 0.5)
        self.assertEqual(fuzzy_set['dog'], 0.8)

    def test_various_membership_values(self):
        set_str = 'C = {<a, 0.0>, <b, 0.25>, <c, 0.5>, <d, 0.75>, <e, 1.0>}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'C')
        self.assertEqual(fuzzy_set['a'], 0.0)
        self.assertEqual(fuzzy_set['b'], 0.25)
        self.assertEqual(fuzzy_set['c'], 0.5)
        self.assertEqual(fuzzy_set['d'], 0.75)
        self.assertEqual(fuzzy_set['e'], 1.0)

    def test_whitespace_variations(self):
        # Test with different spacing
        test_cases = [
            'A={<x1,0.5>,<x2,1.0>}',  # No spaces
            'A = { <x1, 0.5> , <x2, 1.0> }',  # Extra spaces
            'A={ <x1,0.5>,<x2,1.0> }',  # Mixed spacing
            'A  =  {  <x1,  0.5>  ,  <x2,  1.0>  }',  # Lots of spaces
        ]

        for set_str in test_cases:
            with self.subTest(set_str=set_str):
                fuzzy_set = parse_fuzzy_set(set_str)
                self.assertEqual(fuzzy_set.name, 'A')
                self.assertEqual(fuzzy_set['x1'], 0.5)
                self.assertEqual(fuzzy_set['x2'], 1.0)

    def test_invalid_membership_values(self):
        invalid_cases = [
            'A = {<x1, 1.5>}',  # > 1.0
            'A = {<x1, -0.5>}',  # < 0.0
            'A = {<x1, 2>}',  # > 1.0
            'A = {<x1, -1>}',  # < 0.0
        ]

        for set_str in invalid_cases:
            with self.subTest(set_str=set_str):
                with self.assertRaises(Exception):
                    parse_fuzzy_set(set_str)

    def test_invalid_syntax(self):
        invalid_cases = [
            'A = {<x1, 0.5',  # Missing closing brace
            'A = <x1, 0.5>}',  # Missing opening brace
            'A = {x1, 0.5}',  # Missing angle brackets
            'A = {<x1 0.5>}',  # Missing comma
            'A = {<, 0.5>}',  # Missing element name
            'A = {<x1, >}',  # Missing membership value
        ]

        for set_str in invalid_cases:
            with self.subTest(set_str=set_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_set(set_str)

    def test_duplicate_elements(self):
        set_str = 'A = {<x1, 0.5>, <x1, 0.7>}'
        with self.assertRaises(SyntaxError):
            fuzzy_set = parse_fuzzy_set(set_str)

    def test_empty_set(self):
        set_str = 'A = {}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'A')
        self.assertEqual(len(fuzzy_set.elements), 0)

    def test_special_characters_in_element_names(self):
        set_str = 'A = {<x_1, 0.5>, <x-2, 0.3>, <x.3, 0.7>}'
        with self.assertRaises(SyntaxError):
            fuzzy_set = parse_fuzzy_set(set_str)

    def test_numeric_element_names(self):
        set_str = 'B = {<1, 0.2>, <2, 0.8>, <100, 0.5>}'
        with self.assertRaises(SyntaxError):
            fuzzy_set = parse_fuzzy_set(set_str)

    def test_extra_comma(self):
        set_str = 'B = {<a, 0.2>, <b, 0.8>,}'
        with self.assertRaises(SyntaxError):
            fuzzy_set = parse_fuzzy_set(set_str)

    def test_extra_characters(self):
        set_str = 'B = {<a, 0.2>, <b, 0.8>} A'
        with self.assertRaises(SyntaxError):
            fuzzy_set = parse_fuzzy_set(set_str)

    def test_membership_value_precision(self):
        set_str = 'C = {<x1, 0.333333>, <x2, 0.666667>, <x3, 0.999999>}'
        fuzzy_set = parse_fuzzy_set(set_str)
        self.assertEqual(fuzzy_set.name, 'C')
        self.assertAlmostEqual(fuzzy_set['x1'], 0.333333, places=6)
        self.assertAlmostEqual(fuzzy_set['x2'], 0.666667, places=6)
        self.assertAlmostEqual(fuzzy_set['x3'], 0.999999, places=6)

    def test_mixed_valid_invalid_scenarios(self):
        valid_str = 'A = {<x1, 0.0>, <x2, 1.0>}'
        fuzzy_set = parse_fuzzy_set(valid_str)
        self.assertEqual(fuzzy_set.name, 'A')
        self.assertEqual(fuzzy_set['x1'], 0.0)
        self.assertEqual(fuzzy_set['x2'], 1.0)

        invalid_str = 'A = {<x1, 1.5>}'
        with self.assertRaises(ValueError):
            parse_fuzzy_set(invalid_str)