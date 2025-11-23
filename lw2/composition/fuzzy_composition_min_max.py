from decimal import Decimal
from interval import Interval


class FuzzyCompositionMinMax:

    @staticmethod
    def solve(x: Decimal, y: Decimal) -> Decimal:
        result = x + y - Decimal('1')
        return max(Decimal('0'), min(Decimal('1'), result))

    @staticmethod
    def find_x_for_t_eq(y: Decimal, t: Decimal) -> Interval:
        if t < Decimal('0') or t > Decimal('1'):
            return Interval.empty()

        if t == Decimal('0'):
            return Interval(Decimal('0'), Decimal('1') - y)

        if t == Decimal('1'):
            if y == Decimal('1'):
                return Interval(Decimal('1'), Decimal('1'))
            else:
                return Interval.empty()

        x_val = t + Decimal('1') - y

        if Decimal('0') <= x_val <= Decimal('1'):
            return Interval(x_val, x_val)
        else:
            return Interval.empty()

    @staticmethod
    def find_x_for_t_lower_than(y: Decimal, t: Decimal) -> Interval:
        if t < Decimal('0'):
            return Interval.empty()

        if t >= Decimal('1'):
            return Interval(Decimal('0'), Decimal('1'))

        x_upper = min(Decimal('1'), t + Decimal('1') - y)
        return Interval(Decimal('0'), x_upper)