"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Абстрактный класс для представления нечеткой импликации
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from abc import ABC, abstractmethod
from fuzzy_set import FuzzySet


class AbstractFuzzyImplicationSolver(ABC):

    @abstractmethod
    def solve(self, left_set :FuzzySet, right_set :FuzzySet) -> list[list[float]]:
        pass