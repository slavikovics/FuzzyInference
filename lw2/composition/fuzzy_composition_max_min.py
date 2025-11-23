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