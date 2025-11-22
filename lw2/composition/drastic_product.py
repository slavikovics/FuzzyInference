from decimal import Decimal
from interval import Interval


class DrasticProduct:

    @staticmethod
    def solve(x: Decimal, y: Decimal) -> Decimal:
        if max(x, y) == Decimal('1'):
            return min(x, y)
        return Decimal('0')

    @staticmethod
    def find_x_for_t_eq(y: Decimal, t: Decimal) -> Interval:
        if y == Decimal('0'):
            if t == Decimal('0'):
                return Interval(Decimal('0'), Decimal('1'))
            else:
                return Interval.empty()

        if y == Decimal('1'):
            return Interval(t, t)

        if t == Decimal('0'):
            return Interval(Decimal('0'), Decimal('1'), True, False)
        elif t == y:
            return Interval(Decimal('1'), Decimal('1'))
        else:
            return Interval.empty()

    @staticmethod
    def find_x_for_t_lower_than(y: Decimal, t: Decimal) -> Interval:
        if y == Decimal('0'):
            if t == Decimal('0'):
                return Interval(Decimal('0'), Decimal('1'))
            elif t > Decimal('0'):
                return Interval(Decimal('0'), Decimal('1'))
            else:
                return Interval.empty()

        if y == Decimal('1'):
            if t >= Decimal('1'):
                return Interval(Decimal('0'), Decimal('1'))
            else:
                return Interval(Decimal('0'), t)

        if t >= y:
            return Interval(Decimal('0'), Decimal('1'))
        elif t >= Decimal('0'):
            return Interval(Decimal('0'), Decimal('1'), True, False)
        else:
            return Interval.empty()