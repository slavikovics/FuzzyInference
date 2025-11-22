from system import System
from interval import Interval

class Disjunction:
    """Совокупность систем (дизъюнкция систем) для одного y_j"""

    def __init__(self, systems: list[System]):
        self.systems = systems

    def solve_drastic(self) -> list[list[Interval]]:
        """Решает совокупность систем, возвращает все возможные решения"""
        all_solutions = []
        for system in self.systems:
            if not system.is_empty():
                solutions = system.solve_drastic()
                all_solutions.append(solutions)
        return all_solutions

    def __str__(self):
        return '(' + " ||\n ".join(str(system) for system in self.systems) + ')'