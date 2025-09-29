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

#%%
from parser import parse_fuzzy_set, parse_fuzzy_implication

list_of_sets = []
list_of_imps = []

list_of_sets.append(parse_fuzzy_set('A = {<a, 1>, <c, 0>, <b, 0.9>}'))
list_of_sets.append(parse_fuzzy_set('B = {<a, 1>, <c, 0>, <b, 0.9>}'))
list_of_sets.append(parse_fuzzy_set('C = {<a, 1>, <c, 0>, <b, 0.9>}'))

list_of_imps.append(parse_fuzzy_implication('A ~> B'))
list_of_imps.append(parse_fuzzy_implication('B ~> C'))

print(list_of_sets)
print(list_of_imps)