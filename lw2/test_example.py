from system.system import System
from decimal import Decimal
from composition.drastic_product import DrasticProduct
from composition.fuzzy_composition_min_max import FuzzyCompositionMinMax
from composition.fuzzy_composition_max_min import FuzzyCompositionMaxMin


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

    system = System(FuzzyCompositionMinMax, matrix, t_values)
    solutions = system.solve()

    for i, solution in enumerate(solutions):
        print(f"Решение {i + 1}:")
        for var, interval in solution.items():
            print(f"  {var}: {interval}")
        print()


if __name__ == "__main__":
    example_usage()
