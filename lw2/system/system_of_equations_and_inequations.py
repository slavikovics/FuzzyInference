"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для системы уравнений и неравенств
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from typing import Dict
from interval import Interval


class SystemOfEquationsAndInequations:

    def __init__(self, selected_variable: str, t: Decimal, composition, matrix_column: Dict[str, Decimal]):
        self.selected_variable = selected_variable
        self.t = t
        self.composition = composition
        self.matrix_column = matrix_column

    def solve(self) -> Dict[str, Interval]:
        solution = {}
        for x_name, x_val in self.matrix_column.items():
            if x_name == self.selected_variable:
                solution[x_name] = self.composition.find_x_for_t_eq(x_val, self.t)
            else:
                solution[x_name] = self.composition.find_x_for_t_lower_than(x_val, self.t)
        return solution