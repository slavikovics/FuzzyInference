class Interval:
    """Класс для работы с интервалами [lower, upper]"""

    def __init__(self, lower: float, upper: float):
        self._lower = max(0.0, min(lower, 1.0))
        self._upper = max(0.0, min(upper, 1.0))

    def __and__(self, other: 'Interval') -> 'Interval':
        """Пересечение интервалов"""
        if other is None:
            return self
        if not isinstance(other, Interval):
            return NotImplemented

        return Interval(max(self.lower, other.lower), min(self.upper, other.upper))

    def is_empty(self) -> bool:
        """Проверка на пустоту интервала"""
        return self.lower > self.upper

    def contains(self, value: float) -> bool:
        """Проверка, содержит ли интервал значение"""
        return self.lower <= value <= self.upper

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return False
        return (abs(self.lower - other.lower) < 1e-10 and
                abs(self.upper - other.upper) < 1e-10)

    def __str__(self):
        return f"[{self.lower:.2f}, {self.upper:.2f}]"

    def __repr__(self):
        return f"Interval({self.lower:.2f}, {self.upper:.2f})"

    @property
    def lower(self) -> float:
        return self._lower

    @property
    def upper(self) -> float:
        return self._upper