from fuzzy_implication.implication_solver import AbstractFuzzyImplicationSolver
from fuzzy_set import FuzzySet


class GodelImplicationSolver(AbstractFuzzyImplicationSolver):

    def solve(self, left_set: FuzzySet, right_set: FuzzySet) -> list[list[float]]:
        matrix = []

        for x in left_set.elements:
            row = []
            for y in right_set.elements:
                if left_set[x] <= right_set[y]:
                    row.append(1)
                else:
                    row.append(right_set[y])

            matrix.append(row)

        return matrix