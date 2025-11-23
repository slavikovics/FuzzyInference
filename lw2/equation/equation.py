from decimal import Decimal
from interval import Interval


class Equation:
    def __init__(self, tnorm, variable: str, y: Decimal, t: Decimal):
        self.variable = variable
        self.tnorm = tnorm
        self.y = y
        self.t = t
        self.solution = self.solve()

    def solve(self) -> Interval:
        return self.tnorm.find_x_for_t_eq(self.y, self.t)