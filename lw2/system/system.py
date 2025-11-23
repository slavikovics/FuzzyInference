from decimal import Decimal
from typing import List, Dict, Optional
from system.system_of_equations_and_inequations import SystemOfEquationsAndInequations
from system.aggregate import Aggregate
from interval import Interval


class System:

    def __init__(self, tnorm, matrix: Dict[str, Dict[str, Decimal]], t_values: Dict[str, Decimal]):
        self.tnorm = tnorm
        self.matrix = matrix
        self.t_values = t_values
        self.variables = list(matrix.keys())
        self.aggregates = self._create_aggregates()

    def _create_aggregates(self) -> Dict[str, Aggregate]:
        aggregates = {}

        transposed_matrix = {}
        for x, y_values in self.matrix.items():
            for y_id, y_value in y_values.items():
                if y_id not in transposed_matrix:
                    transposed_matrix[y_id] = {}
                transposed_matrix[y_id][x] = y_value

        for y_id, t in self.t_values.items():
            if y_id in transposed_matrix:
                aggregates[y_id] = Aggregate(
                    y_id, t, self.tnorm, transposed_matrix[y_id]
                )

        return aggregates

    def solve(self) -> List[Dict[str, Interval]]:
        if not self.aggregates:
            return []

        combinations = self._get_system_combinations()
        solutions = []

        for combination in combinations:
            solution = self._solve_combination(combination)
            if solution is not None:
                solutions.append(solution)

        return solutions

    def _get_system_combinations(self) -> List[Dict[str, SystemOfEquationsAndInequations]]:
        from itertools import product

        y_systems = {}
        for y_id, aggregate in self.aggregates.items():
            y_systems[y_id] = list(aggregate)

        combinations = []
        for system_tuple in product(*y_systems.values()):
            combination = {}
            for i, y_id in enumerate(self.aggregates.keys()):
                combination[y_id] = system_tuple[i]
            combinations.append(combination)

        return combinations

    def _solve_combination(self, combination: Dict[str, SystemOfEquationsAndInequations]) -> Optional[Dict[str, Interval]]:
        solution = {var: Interval(Decimal('0'), Decimal('1')) for var in self.variables}

        for y_id, system in combination.items():
            system_solution = system.solve()
            for var, interval in system_solution.items():
                if var in solution:
                    solution[var] = solution[var] & interval
                    if solution[var].is_empty():
                        return None

        return solution