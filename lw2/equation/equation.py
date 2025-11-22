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
        """Решает уравнение для t-нормы"""
        if self.eq_type == EquationType.EQUAL:
            return self._solve_equal_drastic()
        else:  # LESS_EQUAL
            return self._solve_less_equal_drastic()

    def _solve_equal_drastic(self) -> Interval:
        """Решает уравнение x /\ a = b для t-нормы"""
        if self.b == 0:
            return Interval(2 - self.b, 1)
        elif self.b == 1:
            return Interval(0, 1 - self.a)
        else:
            return Interval(self.b - self.a + 1, self.b - self.a + 1)

    def _solve_less_equal_drastic(self) -> Interval:
        if self.b == 0:
            return Interval(0, self.b - self.a + 1)
        elif self.b == 1:
            return Interval(0, 1 - self.a)
        else:
            return Interval(0, 1)

    def __str__(self):
        return f"x{self.variable_index + 1} /\\ {self.a:.2f} {self.eq_type.value} {self.b:.2f}"

    def __repr__(self):
        return f"Equation(x{self.variable_index + 1}, a={self.a:.2f}, b={self.b:.2f}, {self.eq_type.value})"