"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для совокупности
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from typing import List, Dict, Tuple, Iterator
from system.system_of_equations_and_inequations import SystemOfEquationsAndInequations


class Aggregate:

    def __init__(self, y_id: str, t: Decimal, composition, matrix_column: Dict[str, Decimal]):
        self.y_id = y_id
        self.t = t
        self.composition = composition
        self.matrix_column = matrix_column
        self.systems = self._create_systems()

    def _create_systems(self) -> List[SystemOfEquationsAndInequations]:
        systems = []
        for variable in self.matrix_column.keys():
            system = SystemOfEquationsAndInequations(
                variable, self.t, self.composition, self.matrix_column
            )
            systems.append(system)
        return systems

    def __iter__(self) -> Iterator[SystemOfEquationsAndInequations]:
        return iter(self.systems)

    def __len__(self) -> int:
        return len(self.systems)
