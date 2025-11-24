"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Пример выполнения обратного нечёткого логического вывода
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from system.system import System
from decimal import Decimal
from composition import DrasticProduct, FuzzyCompositionLukasiewicz, FuzzyCompositionMaxMin


def example_usage():
    matrix = {
        'y1': {'x1': Decimal('0.7'), 'x2': Decimal('0.7')},
        'y2': {'x1': Decimal('0.1'), 'x2': Decimal('0.3')},
        'y3': {'x1': Decimal('0.2'), 'x2': Decimal('0.1')}
    }

    t_values = {
        'y1': Decimal('0.7'),
        'y2': Decimal('0.3'),
        'y3': Decimal('0.2')
    }

    system = System(FuzzyCompositionMaxMin, matrix, t_values)
    solutions = system.solve()

    for i, solution in enumerate(solutions):
        print(f"Решение {i + 1}:")
        for var, interval in solution.items():
            print(f"  {var}: {interval}")
        print()


if __name__ == "__main__":
    example_usage()
