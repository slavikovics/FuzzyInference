"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для тестиования нечёткой композиции
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
import unittest
from decimal import Decimal
from composition.fuzzy_composition_lukasiewicz import FuzzyCompositionLukasiewicz
from interval import Interval


class TestFuzzyComposition(unittest.TestCase):

    def test_solve(self):
        fc = FuzzyCompositionLukasiewicz

        self.assertEqual(fc.solve(Decimal('0'), Decimal('0')), Decimal('0'))
        self.assertEqual(fc.solve(Decimal('1'), Decimal('1')), Decimal('1'))
        self.assertEqual(fc.solve(Decimal('0'), Decimal('1')), Decimal('0'))
        self.assertEqual(fc.solve(Decimal('1'), Decimal('0')), Decimal('0'))

        self.assertEqual(fc.solve(Decimal('0.5'), Decimal('0.5')), Decimal('0'))
        self.assertEqual(fc.solve(Decimal('0.8'), Decimal('0.7')), Decimal('0.5'))
        self.assertEqual(fc.solve(Decimal('0.3'), Decimal('0.9')), Decimal('0.2'))

        self.assertEqual(fc.solve(Decimal('0.8'), Decimal('0.9')), Decimal('0.7'))
        self.assertEqual(fc.solve(Decimal('1'), Decimal('0.5')), Decimal('0.5'))
        self.assertEqual(fc.solve(Decimal('0.5'), Decimal('1')), Decimal('0.5'))

    def test_find_x_for_t_eq(self):
        fc = FuzzyCompositionLukasiewicz

        self.assertEqual(fc.find_x_for_t_eq(Decimal('0.5'), Decimal('0')), Interval(Decimal('0'), Decimal('0.5')))
        self.assertEqual(fc.find_x_for_t_eq(Decimal('0.5'), Decimal('1')), Interval.empty())

        self.assertEqual(fc.find_x_for_t_eq(Decimal('0.5'), Decimal('0.3')), Interval(Decimal('0.8'), Decimal('0.8')))
        self.assertEqual(fc.find_x_for_t_eq(Decimal('0.7'), Decimal('0.5')), Interval(Decimal('0.8'), Decimal('0.8')))

        self.assertTrue(fc.find_x_for_t_eq(Decimal('0.2'), Decimal('0.9')).is_empty())
        self.assertEqual(fc.find_x_for_t_eq(Decimal('0.9'), Decimal('0.2')), Interval(Decimal('0.3'), Decimal('0.3')))

        self.assertEqual(fc.find_x_for_t_eq(Decimal('1'), Decimal('1')), Interval(Decimal('1'), Decimal('1')))
        self.assertEqual(fc.find_x_for_t_eq(Decimal('1'), Decimal('0')), Interval(Decimal('0'), Decimal('0')))

    def test_find_x_for_t_lower_than(self):
        fc = FuzzyCompositionLukasiewicz

        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.5'), Decimal('-0.1')), Interval.empty())
        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.5'), Decimal('1')), Interval(Decimal('0'), Decimal('1')))

        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.5'), Decimal('0.3')), Interval(Decimal('0'), Decimal('0.8')))
        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.7'), Decimal('0.5')), Interval(Decimal('0'), Decimal('0.8')))

        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.5'), Decimal('0')), Interval(Decimal('0'), Decimal('0.5')))
        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.8'), Decimal('0')), Interval(Decimal('0'), Decimal('0.2')))

        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.2'), Decimal('0.9')), Interval(Decimal('0'), Decimal('1')))
        self.assertEqual(fc.find_x_for_t_lower_than(Decimal('0.9'), Decimal('0.2')), Interval(Decimal('0'), Decimal('0.3')))