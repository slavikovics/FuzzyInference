from fuzzy_relation_solver import FuzzyRelationSolver
from data_processor import DataProcessor

def test_example():
    """Тестирование на примере из описания"""
    print("ТЕСТИРОВАНИЕ НА ПРИМЕРЕ:")

    # Данные из примера
    relation_matrix = [
        [0.5, 1.0],
        [1.0, 1.0]
    ]
    output_vector = [0.5, 1.0]

    print(f"Матрица отношений: {relation_matrix}")
    print(f"Выходной вектор: {output_vector}")

    solver = FuzzyRelationSolver(relation_matrix, output_vector)
    solutions = solver.solve_drastic()

    DataProcessor.display_solutions(solutions, relation_matrix, output_vector)

if __name__ == "__main__":
    test_example()