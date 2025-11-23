from decimal import Decimal
from typing import Optional


class Interval:

    def __init__(self, lower: Optional[Decimal], upper: Optional[Decimal], lower_closed: bool = True,
                 upper_closed: bool = True):
        self._lower = lower
        self._upper = upper
        self._lower_closed = lower_closed
        self._upper_closed = upper_closed

    def __and__(self, other: 'Interval') -> 'Interval':
        if not isinstance(other, Interval):
            return NotImplemented

        if self.lower is None or other.lower is None:
            return self.empty()

        new_lower = max(self._lower, other._lower)
        if self._lower == other._lower:
            new_lower_closed = self._lower_closed and other._lower_closed
        elif self._lower > other._lower:
            new_lower_closed = self._lower_closed
        else:
            new_lower_closed = other._lower_closed

        new_upper = min(self._upper, other._upper)

        if self._upper == other._upper:
            new_upper_closed = self._upper_closed and other._upper_closed
        elif self._upper < other._upper:
            new_upper_closed = self._upper_closed
        else:
            new_upper_closed = other._upper_closed

        if new_lower > new_upper or (new_lower == new_upper and (not new_lower_closed or not new_upper_closed)):
            return Interval.empty()

        return Interval(new_lower, new_upper, new_lower_closed, new_upper_closed)

    def is_empty(self) -> bool:
        return self._lower is None

    def contains(self, value: Decimal) -> bool:
        if self.is_empty():
            return False

        lower_check = (value > self._lower) or (value == self._lower and self._lower_closed)
        upper_check = (value < self._upper) or (value == self._upper and self._upper_closed)

        return lower_check and upper_check

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return False

        if self.is_empty() and other.is_empty():
            return True

        return (self._lower == other._lower and
                self._upper == other._upper and
                self._lower_closed == other._lower_closed and
                self._upper_closed == other._upper_closed)

    def __str__(self):
        if self.is_empty():
            return "∅"

        if (self._lower == self._upper and
                self._lower_closed and self._upper_closed):
            return f"{{{self._lower:.1f}}}"

        left_bracket = '[' if self._lower_closed else '('
        right_bracket = ']' if self._upper_closed else ')'
        return f"{left_bracket}{self._lower:.2f}, {self._upper:.2f}{right_bracket}"

    def __repr__(self):
        if self.is_empty():
            return "Interval.empty()"
        return f"Interval({self._lower}, {self._upper}, {self._lower_closed}, {self._upper_closed})"

    @classmethod
    def empty(cls) -> 'Interval':
        empty_interval = cls(Decimal('0'), Decimal('0'))
        empty_interval._lower = None
        empty_interval._upper = None
        return empty_interval

    @property
    def lower(self) -> Decimal:
        return self._lower

    @property
    def upper(self) -> Decimal:
        return self._upper

    @property
    def lower_closed(self) -> bool:
        return self._lower_closed

    @property
    def upper_closed(self) -> bool:
        return self._upper_closed
