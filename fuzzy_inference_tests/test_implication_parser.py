"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Тесты для парсера импликации
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import unittest
from parser import parse_fuzzy_implication


class FuzzyImplicationParserTests(unittest.TestCase):

    def test_names_parsing(self):
        imp_str = 'A ~> B'
        fuzzy_implication = parse_fuzzy_implication(imp_str)
        self.assertEqual(fuzzy_implication.first, 'A')
        self.assertEqual(fuzzy_implication.second, 'B')

        imp_str = 'B ~> A'
        fuzzy_implication = parse_fuzzy_implication(imp_str)
        self.assertEqual(fuzzy_implication.first, 'B')
        self.assertEqual(fuzzy_implication.second, 'A')

    def test_invalid_structure(self):
        imp_str = '~> B'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = 'B ~>'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = '1a ~> b'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = 'A ~ B'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = 'A > B'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = 'A ~> B ~> C'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

        imp_str = '😜 ~> B'
        with self.assertRaises(SyntaxError):
            parse_fuzzy_implication(imp_str)

    def test_whitespace_variations(self):
        test_cases = [
            ('A~>B', 'A', 'B'),
            ('A ~>B', 'A', 'B'),
            ('A~> B', 'A', 'B'),
            ('A  ~>  B', 'A', 'B'),
            ('  A ~> B  ', 'A', 'B'),
            ('\tA ~> B\n', 'A', 'B'),
            ('A   ~>   B', 'A', 'B'),
        ]

        for imp_str, expected_first, expected_second in test_cases:
            with self.subTest(imp_str=imp_str):
                fuzzy_implication = parse_fuzzy_implication(imp_str)
                self.assertEqual(fuzzy_implication.first, expected_first)
                self.assertEqual(fuzzy_implication.second, expected_second)

    def test_single_letter_set_names(self):
        capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for letter1 in capital_letters:
            for letter2 in capital_letters:
                with self.subTest(implication=f"{letter1} ~> {letter2}"):
                    imp_str = f'{letter1} ~> {letter2}'
                    fuzzy_implication = parse_fuzzy_implication(imp_str)
                    self.assertEqual(fuzzy_implication.first, letter1)
                    self.assertEqual(fuzzy_implication.second, letter2)

    def test_invalid_set_names(self):
        invalid_cases = [
            '1A ~> B',
            'A_ ~> B',
            'A- ~> B',
            'A. ~> B',
            '1 ~> B',
            '1 ~> 2',
            '@ ~> B',
        ]

        for imp_str in invalid_cases:
            with self.subTest(imp_str=imp_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_implication_operator_variations(self):
        invalid_operators = [
            'A -> B',
            'A => B',
            'A ==> B',
            'A --> B',
            'A ~~> B',
            'A ~>> B',
            'A <~> B',
        ]

        for imp_str in invalid_operators:
            with self.subTest(imp_str=imp_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_empty_and_whitespace_only_strings(self):
        empty_cases = [
            '',
            '   ',
            ' ~> ',
            '~>',
        ]

        for imp_str in empty_cases:
            with self.subTest(imp_str=repr(imp_str)):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_multiple_implications_in_string(self):
        invalid_cases = [
            'A ~> B ~> C',
            'A ~> B /\\ C ~> D',
            'A ~> B, C ~> D',
            'A ~> B; C ~> D',
        ]

        for imp_str in invalid_cases:
            with self.subTest(imp_str=imp_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_extra_text_around_implication(self):
        invalid_cases = [
            'If A ~> B',
            'A ~> B then',
            'A implies ~> B',
            'A ~> implies B',
            'Set A ~> Set B',
        ]

        for imp_str in invalid_cases:
            with self.subTest(imp_str=imp_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_case_sensitivity(self):
        valid_cases = [
            ('A ~> B', 'A', 'B'),
            ('Z ~> Y', 'Z', 'Y'),
            ('X ~> X', 'X', 'X'),
            ('set ~> X', 'set', 'X'),
            ('Ab ~> s1', 'Ab', 's1'),
        ]

        invalid_cases = [
            '1a ~> 4B',
            '_A ~> b_',
            '123456789a ~> b',
            'Ab ~> C.',
        ]

        # Test valid cases
        for imp_str, exp_first, exp_second in valid_cases:
            with self.subTest(valid_case=imp_str):
                fuzzy_implication = parse_fuzzy_implication(imp_str)
                self.assertEqual(fuzzy_implication.first, exp_first)
                self.assertEqual(fuzzy_implication.second, exp_second)

        # Test invalid cases
        for imp_str in invalid_cases:
            with self.subTest(invalid_case=imp_str):
                with self.assertRaises(SyntaxError):
                    parse_fuzzy_implication(imp_str)

    def test_implication_object_structure(self):
        imp_str = 'A ~> B'
        fuzzy_implication = parse_fuzzy_implication(imp_str)
        self.assertTrue(hasattr(fuzzy_implication, 'first'))
        self.assertTrue(hasattr(fuzzy_implication, 'second'))

        self.assertEqual(fuzzy_implication.first, 'A')
        self.assertEqual(fuzzy_implication.second, 'B')

        self.assertIsInstance(str(fuzzy_implication), str)
        self.assertIsInstance(repr(fuzzy_implication), str)