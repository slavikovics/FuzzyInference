"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для нечёткой композиции (max({min({xi}U{yi})|i}))
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from interval import Interval


class FuzzyCompositionMaxMin:

    @staticmethod
    def solve(x: Decimal, y: Decimal) -> Decimal:
        return max(min(x, y))

    @staticmethod
    def find_x_for_t_eq(y: Decimal, t: Decimal) -> Interval:
        if t < Decimal('0') or t > Decimal('1'):
            return Interval.empty()

        if y < t:
            return Interval.empty()
        elif y == t:
            return Interval(t, Decimal('1'))
        else:
            return Interval(t, t)

    @staticmethod
    def find_x_for_t_lower_than(y: Decimal, t: Decimal) -> Interval:
        if t < Decimal('0'):
            return Interval.empty()

        if t >= Decimal('1'):
            return Interval(Decimal('0'), Decimal('1'))

        if y <= t:
            return Interval(Decimal('0'), Decimal('1'))
        else:
            return Interval(Decimal('0'), t)