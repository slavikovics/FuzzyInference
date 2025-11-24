"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для неравенства
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from interval import Interval


class LessOrEqualInequation:
    def __init__(self, tnorm, variable: str, y: Decimal, t: Decimal):
        self.variable = variable
        self.tnorm = tnorm
        self.y = y
        self.t = t
        self.solution = self.solve()

    def solve(self) -> Interval:
        return self.tnorm.find_x_for_t_lower_than(self.y, self.t)