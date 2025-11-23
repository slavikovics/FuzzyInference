from decimal import Decimal
from typing import List, Dict, Tuple, Iterator
from interval import Interval


class SystemOfEquationsAndInequations:

    def __init__(self, selected_variable: str, t: Decimal, tnorm, matrix_column: Dict[str, Decimal]):
        self.selected_variable = selected_variable
        self.t = t
        self.tnorm = tnorm
        self.matrix_column = matrix_column

    def solve(self) -> Dict[str, Interval]:
        solution = {}
        for x_name, x_val in self.matrix_column.items():
            if x_name == self.selected_variable:
                solution[x_name] = self.tnorm.find_x_for_t_eq(x_val, self.t)
            else:
                solution[x_name] = self.tnorm.find_x_for_t_lower_than(x_val, self.t)
        return solution