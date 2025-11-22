from typing import List, Tuple, Set, Dict, Any, Optional


def main():
    print("АЛГОРИТМ ОБРАТНОГО НЕЧЁТКОГО ЛОГИЧЕСКОГО ВЫВОДА")
    print("Для драстического произведения")
    print("-" * 50)

    matrix, output_vec = DataProcessor.parse_input()

    if not matrix or len(output_vec) != len(matrix[0]):
        print("Ошибка: несоответствие размеров матрицы и вектора!")
        return

    solver = FuzzyRelationSolver(matrix, output_vec)
    solutions = solver.solve_drastic()

    DataProcessor.display_solutions(solutions, matrix, output_vec)





if __name__ == "__main__":
    test_example()
    # print("\n" + "="*50 + "\n")
    # main()