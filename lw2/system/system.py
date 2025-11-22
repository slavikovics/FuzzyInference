from equation import Equation
from interval import Interval

class System:
    """Система уравнений для одного столбца (одного y_j)"""

    def __init__(self, equations: list[Equation]):
        self.equations = equations

    def solve_drastic(self) -> list[Interval]:
        """Решает систему уравнений для драстического произведения"""
        solutions = []
        for eq in self.equations:
            solutions.append(eq.solve_drastic())
        return solutions

    def is_empty(self) -> bool:
        """Проверяет, имеет ли система решение"""
        solutions = self.solve_drastic()
        return any(sol.is_empty() for sol in solutions)

    def __str__(self):
        return " && ".join(str(eq) for eq in self.equations)

    def __repr__(self):
        return f"System({self.equations})"