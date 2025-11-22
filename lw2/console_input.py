from typing import List, Tuple, Set, Dict, Any, Optional


def main():
    """Основная функция"""
    print("АЛГОРИТМ ОБРАТНОГО НЕЧЁТКОГО ЛОГИЧЕСКОГО ВЫВОДА")
    print("Для драстического произведения")
    print("-" * 50)

    # Ввод данных
    matrix, output_vec = DataProcessor.parse_input()

    # Проверка корректности размеров
    if not matrix or len(output_vec) != len(matrix[0]):
        print("Ошибка: несоответствие размеров матрицы и вектора!")
        return

    # Решение
    solver = FuzzyRelationSolver(matrix, output_vec)
    solutions = solver.solve_drastic()

    # Вывод результатов
    DataProcessor.display_solutions(solutions, matrix, output_vec)


# Тестирование на вашем примере



if __name__ == "__main__":
    test_example()
    # print("\n" + "="*50 + "\n")
    # main()