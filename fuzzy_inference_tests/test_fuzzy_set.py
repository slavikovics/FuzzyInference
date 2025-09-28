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
        self.assertNotEqual(a, b)

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
        elems = ["x1", "x2"]
        degs = [0.1, 0.9]
        a = FuzzySet("A", elems, degs)
        elems.append("x3")
        degs.append(0.5)
        # внутреннее состояние не должно было измениться (если реализация копирует данные)
        self.assertEqual(len(a), 2)
        self.assertIn("x1", a)
        self.assertNotIn("x3", a)