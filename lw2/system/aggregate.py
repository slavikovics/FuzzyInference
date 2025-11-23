from decimal import Decimal
from typing import List, Dict, Tuple, Iterator
from system.system_of_equations_and_inequations import SystemOfEquationsAndInequations


class Aggregate:
    """Совокупность систем для одного столбца y"""

    def __init__(self, y_id: str, t: Decimal, tnorm, matrix_row: Dict[str, Decimal]):
        self.y_id = y_id  # Идентификатор столбца (например, 'y1')
        self.t = t  # Целевое значение для этого столбца
        self.tnorm = tnorm
        self.matrix_row = matrix_row  # Значения {x: y} для этого столбца
        self.systems = self._create_systems()

    def _create_systems(self) -> List[SystemOfEquationsAndInequations]:
        """Создает все возможные системы для данного столбца y"""
        systems = []
        for variable in self.matrix_row.keys():
            system = SystemOfEquationsAndInequations(
                variable, self.t, self.tnorm, self.matrix_row
            )
            systems.append(system)
        return systems

    def __iter__(self) -> Iterator[SystemOfEquationsAndInequations]:
        return iter(self.systems)

    def __len__(self) -> int:
        return len(self.systems)
