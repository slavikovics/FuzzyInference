from decimal import Decimal
from typing import List, Dict, Optional
from system.system_of_equations_and_inequations import SystemOfEquationsAndInequations
from system.aggregate import Aggregate
from interval import Interval
from itertools import product


class System:

    def __init__(self, tnorm, transposed_matrix: Dict[str, Dict[str, Decimal]], t_values: Dict[str, Decimal]):
        self.tnorm = tnorm
        self.transposed_matrix = transposed_matrix
        self.t_values = t_values
        self.y_ids = list(t_values.keys())
        self.variables = list(transposed_matrix[self.y_ids[0]].keys()) if self.y_ids else []
        self.aggregates = self._create_aggregates()

    def _create_aggregates(self) -> Dict[str, Aggregate]:
        aggregates = {}
        for y_id, t in self.t_values.items():
            if y_id in self.transposed_matrix:
                aggregates[y_id] = Aggregate(
                    y_id, t, self.tnorm, self.transposed_matrix[y_id]
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

        return System._remove_duplicate_solutions(solutions)

    def _get_system_combinations(self) -> List[Dict[str, SystemOfEquationsAndInequations]]:
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

    @staticmethod
    def _remove_duplicate_solutions(solutions: List[Dict[str, Interval]]) -> List[Dict[str, Interval]]:
        unique_solutions = []
        for solution in solutions:
            if not any(System._are_solutions_equal(solution, existing) for existing in unique_solutions):
                unique_solutions.append(solution)
        return unique_solutions

    @staticmethod
    def _are_solutions_equal(sol1: Dict[str, Interval], sol2: Dict[str, Interval]) -> bool:
        if set(sol1.keys()) != set(sol2.keys()):
            return False
        for var in sol1:
            if sol1[var] != sol2[var]:
                return False
        return True