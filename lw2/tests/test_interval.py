import unittest
from decimal import Decimal
from interval import Interval


class TestInterval(unittest.TestCase):

    def test_creation(self):
        interval1 = Interval(Decimal('0'), Decimal('1'))
        self.assertEqual(interval1.lower, Decimal('0'))
        self.assertEqual(interval1.upper, Decimal('1'))
        self.assertTrue(interval1.lower_closed)
        self.assertTrue(interval1.upper_closed)
        self.assertFalse(interval1.is_empty())

        interval2 = Interval(Decimal('0'), Decimal('1'), False, False)
        self.assertFalse(interval2.lower_closed)
        self.assertFalse(interval2.upper_closed)

        interval3 = Interval(Decimal('0'), Decimal('1'), True, False)
        self.assertTrue(interval3.lower_closed)
        self.assertFalse(interval3.upper_closed)

    def test_empty_interval(self):
        empty = Interval.empty()
        self.assertTrue(empty.is_empty())
        self.assertEqual(empty, Interval.empty())

    def test_contains(self):
        closed = Interval(Decimal('0'), Decimal('1'))
        self.assertTrue(closed.contains(Decimal('0')))
        self.assertTrue(closed.contains(Decimal('0.5')))
        self.assertTrue(closed.contains(Decimal('1')))
        self.assertFalse(closed.contains(Decimal('-0.1')))
        self.assertFalse(closed.contains(Decimal('1.1')))

        open_interval = Interval(Decimal('0'), Decimal('1'), False, False)
        self.assertFalse(open_interval.contains(Decimal('0')))
        self.assertTrue(open_interval.contains(Decimal('0.5')))
        self.assertFalse(open_interval.contains(Decimal('1')))

        half_open_low = Interval(Decimal('0'), Decimal('1'), False, True)
        self.assertFalse(half_open_low.contains(Decimal('0')))
        self.assertTrue(half_open_low.contains(Decimal('0.5')))
        self.assertTrue(half_open_low.contains(Decimal('1')))

        half_open_high = Interval(Decimal('0'), Decimal('1'), True, False)
        self.assertTrue(half_open_high.contains(Decimal('0')))
        self.assertTrue(half_open_high.contains(Decimal('0.5')))
        self.assertFalse(half_open_high.contains(Decimal('1')))

        empty = Interval.empty()
        self.assertFalse(empty.contains(Decimal('0')))
        self.assertFalse(empty.contains(Decimal('0.5')))

    def test_intersection(self):
        a = Interval(Decimal('0'), Decimal('2'))
        b = Interval(Decimal('1'), Decimal('3'))
        result = a & b
        self.assertEqual(result, Interval(Decimal('1'), Decimal('2')))

        c = Interval(Decimal('0.5'), Decimal('1.5'))
        d = Interval(Decimal('0'), Decimal('2'))
        result2 = c & d
        self.assertEqual(result2, Interval(Decimal('0.5'), Decimal('1.5')))

        e = Interval(Decimal('0'), Decimal('1'))
        f = Interval(Decimal('1'), Decimal('2'))
        result3 = e & f
        self.assertEqual(result3, Interval(Decimal('1'), Decimal('1')))

        g = Interval(Decimal('0'), Decimal('1'))
        h = Interval(Decimal('2'), Decimal('3'))
        result4 = g & h
        self.assertTrue(result4.is_empty())

    def test_intersection_with_open_close(self):
        a = Interval(Decimal('0'), Decimal('2'), False, True)
        b = Interval(Decimal('1'), Decimal('3'), True, True)
        result = a & b
        self.assertEqual(result, Interval(Decimal('1'), Decimal('2'), True, True))

        c = Interval(Decimal('0'), Decimal('2'), False, False)
        d = Interval(Decimal('1'), Decimal('3'), False, False)
        result2 = c & d
        self.assertEqual(result2, Interval(Decimal('1'), Decimal('2'), False, False))

        e = Interval(Decimal('0'), Decimal('1'), True, False)
        f = Interval(Decimal('1'), Decimal('2'), False, True)
        result3 = e & f
        self.assertTrue(result3.is_empty())

    def test_edge_cases_intersection(self):
        a = Interval(Decimal('0'), Decimal('1'))
        result = a & a
        self.assertEqual(result, a)

        b = Interval(Decimal('0'), Decimal('1'), False, False)
        result2 = b & b
        self.assertEqual(result2, b)

    def test_equality(self):
        a = Interval(Decimal('0'), Decimal('1'))
        b = Interval(Decimal('0'), Decimal('1'))
        c = Interval(Decimal('0'), Decimal('1'), False, False)
        d = Interval(Decimal('0'), Decimal('2'))

        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(a, d)
        self.assertEqual(Interval.empty(), Interval.empty())

    def test_string_representation(self):
        closed = Interval(Decimal('0'), Decimal('1'))
        self.assertIn('[0, 1]', str(closed))

        open_interval = Interval(Decimal('0.1'), Decimal('0.0001'), False, False)
        self.assertIn('(0.1, 0.0001)', str(open_interval))

        half_open = Interval(Decimal('0.9999999999999999999999999999'), Decimal('1'), True, False)
        self.assertIn('[0.9999999999999999999999999999, 1)', str(half_open))

        empty = Interval.empty()
        self.assertEqual('∅', str(empty))

    def test_single_point_interval(self):
        point = Interval(Decimal('0.5'), Decimal('0.5'))
        self.assertFalse(point.is_empty())
        self.assertTrue(point.contains(Decimal('0.5')))
        self.assertFalse(point.contains(Decimal('0.4')))
        self.assertFalse(point.contains(Decimal('0.6')))