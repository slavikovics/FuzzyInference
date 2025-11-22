from disjunction import Disjunction
from equation import Equation, EquationType
from system import System
from interval import Interval

import itertools

class FuzzyRelationSolver:
    """Оркестратор для решения обратной задачи нечеткого логического вывода"""

    def __init__(self, relation_matrix: list[list[float]], output_vector: list[float]):
        self.relation_matrix = relation_matrix
        self.output_vector = output_vector
        self.num_x = len(relation_matrix)
        self.num_y = len(relation_matrix[0]) if relation_matrix else 0

    def create_disjunctions_for_all_y(self) -> list[Disjunction]:
        """Создает совокупности систем для всех y_j"""
        disjunctions = []

        for j in range(self.num_y):
            b_j = self.output_vector[j]
            systems_for_yj = []

            # Генерируем все возможные случаи для max(t1, t2, ..., tn) = b_j
            # Каждый случай: один t_k = b_j, остальные <= b_j
            for k in range(self.num_x):
                equations = []
                for i in range(self.num_x):
                    a_ij = self.relation_matrix[i][j]
                    if i == k:
                        # Этот t должен быть равен b_j
                        equations.append(Equation(i, a_ij, b_j, EquationType.EQUAL))
                    else:
                        # Остальные t должны быть <= b_j
                        equations.append(Equation(i, a_ij, b_j, EquationType.LESS_EQUAL))

                systems_for_yj.append(System(equations))

            disjunctions.append(Disjunction(systems_for_yj))

        return disjunctions

    def solve_drastic(self) -> list[list[Interval]]:
        """Решает полную систему для драстического произведения"""
        disjunctions = self.create_disjunctions_for_all_y()

        # Получаем все возможные решения для каждого y_j
        all_y_solutions = []
        for disj in disjunctions:
            y_solutions = disj.solve_drastic()
            all_y_solutions.append(y_solutions)

        # Находим пересечения решений для всех y_j
        final_solutions = self._intersect_solutions(all_y_solutions)
        return final_solutions

    def _intersect_solutions(self, all_y_solutions: list[list[list[Interval]]]) -> list[list[Interval]]:
        """Находит пересечения решений для всех y_j"""
        if not all_y_solutions:
            return []

        # Генерируем все возможные комбинации решений для разных y_j
        solution_combinations = list(itertools.product(*all_y_solutions))

        final_solutions = []
        for combination in solution_combinations:
            # combination - это кортеж списков интервалов для каждого y_j
            # Находим пересечение интервалов для каждой переменной x_i
            num_vars = len(combination[0])
            intersection = [Interval(0, 1) for _ in range(num_vars)]  # начальный интервал

            for y_solution in combination:
                for i in range(num_vars):
                    intersection[i] = intersection[i] & y_solution[i]

            # Проверяем, что пересечение не пустое
            if not any(interval.is_empty() for interval in intersection):
                # Убираем дубликаты
                if intersection not in final_solutions:
                    final_solutions.append(intersection)

        return final_solutions