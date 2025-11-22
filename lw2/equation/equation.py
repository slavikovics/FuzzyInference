from equation.equation_type import EquationType
from interval import Interval

class Equation:
    """Класс для представления уравнения x_i /\ a = b"""

    def __init__(self, variable_index: int, a: float, b: float, eq_type: EquationType):
        self.variable_index = variable_index
        self.a = a
        self.b = b
        self.eq_type = eq_type

    def solve_drastic(self) -> Interval:
        """Решает уравнение для драстического произведения"""
        if self.eq_type == EquationType.EQUAL:
            return self._solve_equal_drastic()
        else:  # LESS_EQUAL
            return self._solve_less_equal_drastic()

    def _solve_equal_drastic(self) -> Interval:
        """Решает уравнение x /\ a = b для драстического произведения"""
        if self.a == 0:
            # x /\ 0 = b -> возможно только если b = 0
            return Interval(1, 1) if self.b == 0 else Interval(1, 0)  # пустой

        if self.a == 1:
            # x /\ 1 = b -> x = b
            return Interval(self.b, self.b)

        # a ∈ (0, 1)
        if self.b == 0:
            # x /\ a = 0 -> x ∈ [0, 1] кроме случая когда оба > 0
            # В драстическом: min(x,a) = 0 только если x=0 ИЛИ a=0, но a>0 -> x=0
            return Interval(0, 0)
        elif self.b == self.a:
            # x /\ a = a -> x ∈ [a, 1]
            return Interval(self.a, 1)
        elif 0 < self.b < self.a:
            # Невозможно для драстического произведения
            return Interval(1, 0)  # пустой
        else:
            return Interval(1, 0)  # пустой

    def _solve_less_equal_drastic(self) -> Interval:
        """Решает неравенство x /\ a <= b для драстического произведения"""
        if self.b == 1:
            # x /\ a <= 1 -> всегда истинно
            return Interval(0, 1)

        if self.a == 0:
            # x /\ 0 <= b -> всегда истинно если b >= 0
            return Interval(0, 1) if self.b >= 0 else Interval(1, 0)

        if self.a == 1:
            # x /\ 1 <= b -> x <= b
            return Interval(0, self.b)

        # a ∈ (0, 1)
        if self.b == 0:
            # x /\ a <= 0 -> x = 0
            return Interval(0, 0)
        elif self.b >= self.a:
            # x /\ a <= b (где b >= a) -> x ∈ [0, 1]
            return Interval(0, 1)
        else:  # 0 < b < a
            # x /\ a <= b -> x <= b
            return Interval(0, self.b)

    def __str__(self):
        return f"x{self.variable_index + 1} /\\ {self.a:.2f} {self.eq_type.value} {self.b:.2f}"

    def __repr__(self):
        return f"Equation(x{self.variable_index + 1}, a={self.a:.2f}, b={self.b:.2f}, {self.eq_type.value})"