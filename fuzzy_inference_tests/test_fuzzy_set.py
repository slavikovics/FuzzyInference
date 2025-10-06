"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Тесты для нечёткого множества
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import unittest
from fuzzy_set import FuzzySet


class TestFuzzySet(unittest.TestCase):
    def test_init_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            FuzzySet("A", ["x1", "x2"], [0.1])  # длины 2 != 1

    def test_basic_properties_and_access(self):
        elements = ["x1", "x2", "x3"]
        degrees = [0.0, 0.5, 1.0]
        fs = FuzzySet("A", elements, degrees)

        self.assertEqual(len(fs), 3)

        self.assertIn("x1", fs)
        self.assertNotIn("unknown", fs)

        self.assertEqual(fs["x1"], 0.0)
        self.assertEqual(fs["x2"], 0.5)
        self.assertEqual(fs["x3"], 1.0)
        with self.assertRaises(KeyError):
            _ = fs["not_exist"]

        expected_items = {("x1", 0.0), ("x2", 0.5), ("x3", 1.0)}
        self.assertEqual(fs.items, expected_items)

        self.assertEqual(set(fs.elements), set(elements))
        self.assertEqual(set(fs.degrees_of_membership), set(degrees))

    def test_eq_same_order(self):
        a = FuzzySet("A", ["x1", "x2"], [0.2, 0.8])
        b = FuzzySet("A", ["x1", "x2"], [0.2, 0.8])
        self.assertEqual(a, b)

    def test_eq_different_order(self):
        a = FuzzySet("A", ["x1", "x2", "x3"], [0.1, 0.2, 0.3])
        b = FuzzySet("A", ["x3", "x2", "x1"], [0.3, 0.2, 0.1])
        self.assertEqual(a, b)

    def test_eq_name_mismatch(self):
        a = FuzzySet("A", ["x1"], [0.5])
        b = FuzzySet("B", ["x1"], [0.5])
        self.assertEqual(a, b)

    def test_eq_keys_mismatch(self):
        a = FuzzySet("A", ["x1", "x2"], [0.2, 0.3])
        b = FuzzySet("A", ["x1", "x3"], [0.2, 0.3])
        self.assertNotEqual(a, b)

    def test_eq_float_tolerance(self):
        a = FuzzySet("A", ["x1", "x2"], [0.3, 0.7])
        b = FuzzySet("A", ["x1", "x2"], [0.30000000000000004, 0.7000000000000001])
        self.assertEqual(a, b)

        c = FuzzySet("A", ["x1", "x2"], [0.31, 0.7])
        self.assertNotEqual(a, c)

    def test_is_like(self):
        a = FuzzySet("A", ["x1", "x2"], [0.1, 0.9])
        b = FuzzySet("B", ["x2", "x1"], [0.9, 0.1])
        self.assertTrue(a.is_like(b))

        c = FuzzySet("C", ["x1", "x3"], [0.1, 0.2])
        self.assertFalse(a.is_like(c))

    def test_empty_set(self):
        a = FuzzySet("Empty", [], [])
        self.assertEqual(len(a), 0)
        self.assertEqual(a.items, set())
        self.assertEqual(a.elements, [])
        self.assertEqual(a.degrees_of_membership, [])

    def test_repr_and_str_contains_name(self):
        a = FuzzySet("A", ["x1"], [0.5])
        s = str(a)
        self.assertIn("A", s)
        self.assertIn("x1", s)

    def test_mutation_independence(self):
        elements = ["x1", "x2"]
        degrees = [0.1, 0.9]
        a = FuzzySet("A", elements, degrees)
        elements.append("x3")
        degrees.append(0.5)

        self.assertEqual(len(a), 2)
        self.assertIn("x1", a)
        self.assertNotIn("x3", a)

    def test_set_order(self):
        elements = ['x1', 'x2']
        fuzzy_set = FuzzySet('A', elements, [1, 1])
        order = fuzzy_set.get_set_order()

        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_with_single_element(self):
        elements = ['x1']
        fuzzy_set = FuzzySet('A', elements, [0.5])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        self.assertEqual(elements[0], order[0])

    def test_set_order_with_multiple_elements(self):
        elements = ['x1', 'x2', 'x3', 'x4', 'x5']
        fuzzy_set = FuzzySet('B', elements, [0.1, 0.5, 0.8, 0.3, 0.9])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_with_string_elements(self):
        elements = ['low', 'medium', 'high']
        fuzzy_set = FuzzySet('Temperature', elements, [0.2, 0.7, 0.9])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_with_numeric_elements(self):
        elements = [1, 2, 3, 4, 5]
        fuzzy_set = FuzzySet('NumericSet', elements, [0.1, 0.4, 0.6, 0.8, 1.0])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_with_mixed_elements(self):
        elements = ['x1', 2, 'medium', 4.5]
        fuzzy_set = FuzzySet('MixedSet', elements, [0.3, 0.6, 0.8, 0.1])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_empty_set(self):
        elements = []
        fuzzy_set = FuzzySet('EmptySet', elements, [])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        self.assertEqual({}, order)

    def test_set_order_preserves_original_order(self):
        elements = ['z', 'a', 'm', 'b']
        fuzzy_set = FuzzySet('UnorderedSet', elements, [0.3, 0.6, 0.1, 0.9])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_with_special_characters(self):
        elements = ['x₁', 'x₂', 'x₃', 'α', 'β']
        fuzzy_set = FuzzySet('SpecialSet', elements, [0.2, 0.5, 0.8, 0.4, 0.7])
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])

    def test_set_order_large_set(self):
        elements = [f'x{i}' for i in range(100)]
        membership_values = [i / 100 for i in range(100)]
        fuzzy_set = FuzzySet('LargeSet', elements, membership_values)
        order = fuzzy_set.get_set_order()

        self.assertEqual(len(elements), len(order))
        for index in range(len(elements)):
            self.assertEqual(elements[index], order[index])