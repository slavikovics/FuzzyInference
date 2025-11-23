from decimal import Decimal
from typing import List, Dict, Optional
from system import System
from interval import Interval
from composition import DrasticProduct
from composition import FuzzyCompositionMinMax


def read_input(filename: str) -> tuple:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        raise ValueError(f"Файл {filename} не найден")
    except Exception as e:
        raise ValueError(f"Ошибка чтения файла: {e}")

    if len(lines) < 5:
        raise ValueError("Недостаточно строк во входном файле")

    premise = lines[0]
    if not premise:
        raise ValueError("Первая строка (PREMISE) не может быть пустой")

    y_ids = lines[1].split()
    if not y_ids:
        raise ValueError("Вторая строка (идентификаторы y) не может быть пустой")

    t_values_str = lines[2].split()
    if len(t_values_str) != len(y_ids):
        raise ValueError(f"Количество значений t ({len(t_values_str)}) не совпадает с количеством y ({len(y_ids)})")

    try:
        t_values = {y_id: Decimal(t_str) for y_id, t_str in zip(y_ids, t_values_str)}
    except Exception as e:
        raise ValueError(f"Ошибка преобразования значений t: {e}")

    for y_id, t in t_values.items():
        if t < Decimal('0') or t > Decimal('1'):
            raise ValueError(f"Значение t для {y_id} = {t} должно быть в интервале [0, 1]")

    x_ids = lines[3].split()
    if not x_ids:
        raise ValueError("Четвертая строка (идентификаторы x) не может быть пустой")

    matrix_lines = lines[4:]
    if len(matrix_lines) != len(y_ids):
        raise ValueError(f"Количество строк матрицы ({len(matrix_lines)}) не совпадает с количеством y ({len(x_ids)})")

    matrix = {}
    try:
        for i, y_id in enumerate(y_ids):
            values_str = matrix_lines[i].split()
            if len(values_str) != len(x_ids):
                raise ValueError(
                    f"Количество значений в строке для {y_id} ({len(values_str)}) не совпадает с количеством x ({len(x_ids)})")

            row_values = {}
            for j, x_id in enumerate(x_ids):
                value = Decimal(values_str[j])
                if value < Decimal('0') or value > Decimal('1'):
                    raise ValueError(f"Значение матрицы для {y_id},{x_id} = {value} должно быть в интервале [0, 1]")
                row_values[x_id] = value

            matrix[y_id] = row_values
    except Exception as e:
        raise ValueError(f"Ошибка преобразования матрицы: {e}")

    return premise, y_ids, t_values, x_ids, matrix


def solution_to_str(solution: Dict[str, Interval], x_ids: List[str]) -> str:
    intervals = [str(solution[x_id]) for x_id in x_ids]
    return "(" + " X ".join(intervals) + ")"


def format_output(premise: str, solutions: List[Dict[str, Interval]], x_ids: List[str]) -> str:
    if not solutions:
        solutions_union = "∅"

    else:

        solution_strs = [solution_to_str(solution, x_ids) for solution in solutions]
        solutions_union = " U ".join(solution_strs)

    premise_vars = ", ".join([f"{premise}({x_id})" for x_id in x_ids])
    return f"{solutions_union} э <{premise_vars}>"


def write_output(filename: str, output_str: str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(output_str)
    except Exception as e:
        raise ValueError(f"Ошибка записи в файл {filename}: {e}")


def main():
    try:
        premise, y_ids, t_values, x_ids, matrix = read_input('input.txt')
        tnorm = FuzzyCompositionMinMax()
        system = System(tnorm, matrix, t_values)
        solutions = system.solve()
        output_str = format_output(premise, solutions, x_ids)
        write_output('output.txt', output_str)
        print("Результат успешно записан в output.txt")
        print(output_str)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
