from decimal import Decimal
from typing import List, Dict, Tuple, Iterator
from interval import Interval


class SystemOfEquationsAndInequations:

    def __init__(self, selected_variable: str, t: Decimal, tnorm, matrix_row: Dict[str, Decimal]):
        self.selected_variable = selected_variable
        self.t = t
        self.tnorm = tnorm
        self.matrix_row = matrix_row

    def solve(self) -> Dict[str, Interval]:
        solution = {}
        for x, y_val in self.matrix_row.items():
            if x == self.selected_variable:
                solution[x] = self.tnorm.find_x_for_t_eq(y_val, self.t)
            else:
                solution[x] = self.tnorm.find_x_for_t_lower_than(y_val, self.t)
        return solution