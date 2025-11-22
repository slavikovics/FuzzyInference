from interval import Interval

class DataProcessor:
    """Класс для ввода и вывода данных"""

    @staticmethod
    def parse_input() -> tuple[list[list[float]], list[float]]:
        """Парсит входные данные"""
        print("Введите матрицу нечётких отношений (по строкам, через пробел):")
        matrix = []
        while True:
            line = input().strip()
            if not line:
                break
            row = list(map(float, line.split()))
            matrix.append(row)

        print("Введите вектор результата (через пробел):")
        output_vec = list(map(float, input().split()))

        return matrix, output_vec

    @staticmethod
    def display_solutions(solutions: list[list[Interval]], relation_matrix: list[list[float]],
                          output_vector: list[float]):
        """Выводит решения в читаемом формате"""
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ РЕШЕНИЯ")
        print("=" * 50)

        print(f"Матрица отношений R:")
        for i, row in enumerate(relation_matrix):
            print(f"x{i + 1}: {row}")

        print(f"\nВыходной вектор B: {output_vector}")

        if not solutions:
            print("\nРешений нет!")
            return

        print(f"\nНайдено {len(solutions)} решение(ий):")
        for idx, solution in enumerate(solutions, 1):
            print(f"\nРешение {idx}:")
            for i, interval in enumerate(solution):
                if interval.lower == interval.upper:
                    print(f"  x{i + 1} = {interval.lower:.2f}")
                else:
                    print(f"  x{i + 1} ∈ {interval}")