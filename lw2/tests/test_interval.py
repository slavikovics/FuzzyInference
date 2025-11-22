import unittest
from interval.interval import Interval

class TestInterval(unittest.TestCase):
    def test_interval_initialization_within_bounds(self):
        interval = Interval(0.2, 0.8)
        self.assertAlmostEqual(interval.lower, 0.2)
        self.assertAlmostEqual(interval.upper, 0.8)

    def test_interval_initialization_out_of_bounds(self):
        interval = Interval(-0.5, 1.5)
        self.assertAlmostEqual(interval.lower, 0.0)
        self.assertAlmostEqual(interval.upper, 1.0)

    def test_intersection_of_overlapping_intervals(self):
        interval1 = Interval(0.2, 0.6)
        interval2 = Interval(0.4, 0.8)
        result = interval1 & interval2
        self.assertEqual(result, Interval(0.4, 0.6))

    def test_intersection_of_non_overlapping_intervals(self):
        interval1 = Interval(0.1, 0.3)
        interval2 = Interval(0.4, 0.6)
        result = interval1 & interval2
        self.assertTrue(result.is_empty())

    def test_intersection_with_none(self):
        interval = Interval(0.2, 0.5)
        result = interval & None
        self.assertEqual(result, interval)

    def test_contains_value_within_interval(self):
        interval = Interval(0.3, 0.7)
        self.assertTrue(interval.contains(0.5))

    def test_contains_value_outside_interval(self):
        interval = Interval(0.3, 0.7)
        self.assertFalse(interval.contains(0.8))

    def test_empty_interval_check(self):
        interval = Interval(0.1, 0.3) & Interval(0.4, 0.6)
        self.assertTrue(interval.is_empty())

    def test_equality_of_identical_intervals(self):
        interval1 = Interval(0.2, 0.6)
        interval2 = Interval(0.2, 0.6)
        self.assertEqual(interval1, interval2)

    def test_equality_of_different_intervals(self):
        interval1 = Interval(0.2, 0.6)
        interval2 = Interval(0.3, 0.7)
        self.assertNotEqual(interval1, interval2)

    def test_string_representation_of_interval(self):
        interval = Interval(0.2, 0.6)
        self.assertEqual(str(interval), "[0.20, 0.60]")

    def test_interval_crossing_1(self):
        interval1 = Interval(0.0, 0.5)
        interval2 = Interval(0.5, 1.0)
        result = interval1 & interval2
        self.assertEqual(result, Interval(0.5, 0.5))

    def test_interval_crossing_2(self):
        interval1 = Interval(0.0, 0.7)
        interval2 = Interval(0.3, 1.0)
        result = interval1 & interval2
        self.assertEqual(result, Interval(0.3, 0.7))

    def test_interval_crossing_3(self):
        interval1 = Interval(0.4, 0.9)
        interval2 = Interval(0.1, 0.5)
        result = interval1 & interval2
        self.assertEqual(result, Interval(0.4, 0.5))

    def test_interval_crossing_4(self):
        interval1 = Interval(0.0, 0.2)
        interval2 = Interval(0.3, 0.4)
        result = interval1 & interval2
        self.assertTrue(result.is_empty())

    def test_interval_crossing_5(self):
        interval1 = Interval(0.6, 1.0)
        interval2 = Interval(0.0, 0.5)
        result = interval1 & interval2
        self.assertTrue(result.is_empty())
