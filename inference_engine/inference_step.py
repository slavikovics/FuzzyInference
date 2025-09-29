"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Главное меню программы
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_set import FuzzySet
from fuzzy_implication import ImplicationScheme


class InferenceStep:
    def __init__(self, left_set, implication_scheme, result, equal_to = None):
        self.left_set = left_set
        self.implication_scheme = implication_scheme
        self.result = result
        self.equal_to = equal_to

    def __str__(self):
        if self.equal_to is None:
            return '{ ' + self.left_set.name + ', ' + str(self.implication_scheme) + ' }' + f' |~ {self.result}'
        else:
            return '{ ' + self.left_set.name + ', ' + str(self.implication_scheme) + ' }' + f' |~ {self.result} = {self.equal_to.name}'
