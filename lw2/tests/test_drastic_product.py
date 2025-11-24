"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для тестирования драстического произведения
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
import unittest
from decimal import Decimal
from interval import Interval
from composition.drastic_product import DrasticProduct


class TestDrasticProduct(unittest.TestCase):

    def test_solve(self):
        dp = DrasticProduct

        self.assertEqual(dp.solve(Decimal('0'), Decimal('0')), Decimal('0'))
        self.assertEqual(dp.solve(Decimal('1'), Decimal('1')), Decimal('1'))
        self.assertEqual(dp.solve(Decimal('0'), Decimal('1')), Decimal('0'))
        self.assertEqual(dp.solve(Decimal('1'), Decimal('0')), Decimal('0'))

        self.assertEqual(dp.solve(Decimal('0.5'), Decimal('1')), Decimal('0.5'))
        self.assertEqual(dp.solve(Decimal('1'), Decimal('0.3')), Decimal('0.3'))

        self.assertEqual(dp.solve(Decimal('0.5'), Decimal('0.5')), Decimal('0'))
        self.assertEqual(dp.solve(Decimal('0.2'), Decimal('0.8')), Decimal('0'))

    def test_find_x_for_t_eq(self):
        dp = DrasticProduct

        self.assertEqual(dp.find_x_for_t_eq(Decimal('0'), Decimal('0')), Interval(Decimal('0'), Decimal('1')))
        self.assertTrue(dp.find_x_for_t_eq(Decimal('0'), Decimal('0.5')).is_empty())

        self.assertEqual(dp.find_x_for_t_eq(Decimal('1'), Decimal('0.7')), Interval(Decimal('0.7'), Decimal('0.7')))
        self.assertEqual(dp.find_x_for_t_eq(Decimal('1'), Decimal('1')), Interval(Decimal('1'), Decimal('1')))
        self.assertEqual(dp.find_x_for_t_eq(Decimal('1'), Decimal('0')), Interval(Decimal('0'), Decimal('0')))

        self.assertEqual(dp.find_x_for_t_eq(Decimal('0.5'), Decimal('0')), Interval(Decimal('0'), Decimal('1'), True, False))
        self.assertEqual(dp.find_x_for_t_eq(Decimal('0.5'), Decimal('0.5')), Interval(Decimal('1'), Decimal('1')))
        self.assertTrue(dp.find_x_for_t_eq(Decimal('0.5'), Decimal('0.3')).is_empty())

    def test_find_x_for_t_lower_than(self):
        dp = DrasticProduct

        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('0'), Decimal('0')), Interval(Decimal('0'), Decimal('1')))
        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('0'), Decimal('0.5')), Interval(Decimal('0'), Decimal('1')))

        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('1'), Decimal('0.7')), Interval(Decimal('0'), Decimal('0.7')))
        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('1'), Decimal('1')), Interval(Decimal('0'), Decimal('1')))

        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('0.5'), Decimal('0.3')), Interval(Decimal('0'), Decimal('1'), True, False))
        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('0.5'), Decimal('0.5')), Interval(Decimal('0'), Decimal('1')))
        self.assertEqual(dp.find_x_for_t_lower_than(Decimal('0.5'), Decimal('0.6')), Interval(Decimal('0'), Decimal('1')))

        self.assertTrue(dp.find_x_for_t_lower_than(Decimal('0.5'), Decimal('-0.1')).is_empty())