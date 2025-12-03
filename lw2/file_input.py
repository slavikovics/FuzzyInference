"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Моудуль для ввода данных из файла и вывода решения в файл
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from typing import List, Dict, Tuple, Union, Optional
from system import System
from interval import Interval
from composition import DrasticProduct
from composition import FuzzyCompositionLukasiewicz
from composition import FuzzyCompositionMaxMin


def read_file_contents(filename: str) -> Tuple[bool, Union[List[str], str]]:
    file_obj = open(filename, 'r', encoding='utf-8')
    if file_obj is None:
        return False, f"Файл {filename} не найден"

    lines = []
    for line in file_obj:
        stripped_line = line.strip()
        if stripped_line:
            lines.append(stripped_line)

    file_obj.close()
    return True, lines


def validate_basic_structure(lines: List[str]) -> Tuple[bool, Optional[str]]:
    if len(lines) < 5:
        return False, "Недостаточно строк во входном файле"
    return True, None


def parse_premise(line: str) -> Tuple[bool, Union[str, None]]:
    if not line:
        return False, "Первая строка (PREMISE) не может быть пустой"
    return True, line


def parse_y_ids(line: str) -> Tuple[bool, Union[List[str], str]]:
    ids = line.split()
    if not ids:
        return False, "Вторая строка не может быть пустой"
    return True, ids


def parse_t_values(line: str, y_ids: List[str]) -> Tuple[bool, Union[Dict[str, Decimal], str]]:
    values_str = line.split()
    if len(values_str) != len(y_ids):
        return False, f"Количество значений t ({len(values_str)}) не совпадает с количеством y ({len(y_ids)})"

    t_values = {}
    for i, (y_id, t_str) in enumerate(zip(y_ids, values_str)):
        try:
            value = Decimal(t_str)
        except:
            return False, f"Ошибка преобразования значения t: {t_str}"

        if value < Decimal('0') or value > Decimal('1'):
            return False, f"Значение t для {y_id} = {value} должно быть в интервале [0, 1]"
        t_values[y_id] = value

    return True, t_values


def parse_x_ids(line: str) -> Tuple[bool, Union[List[str], str]]:
    ids = line.split()
    if not ids:
        return False, "Четвертая строка (идентификаторы x) не может быть пустой"
    return True, ids


def parse_matrix(lines: List[str], y_ids: List[str], x_ids: List[str]) -> Tuple[
    bool, Union[Dict[str, Dict[str, Decimal]], str]]:
    if len(lines) != len(y_ids):
        return False, f"Количество строк матрицы ({len(lines)}) не совпадает с количеством y ({len(y_ids)})"

    matrix = {}
    for i, y_id in enumerate(y_ids):
        values_str = lines[i].split()
        if len(values_str) != len(x_ids):
            return False, f"Количество значений в строке для {y_id} ({len(values_str)}) не совпадает с количеством x ({len(x_ids)})"

        row_values = {}
        for j, x_id in enumerate(x_ids):
            try:
                value = Decimal(values_str[j])
            except:
                return False, f"Ошибка преобразования значения матрицы: {values_str[j]}"

            if value < Decimal('0') or value > Decimal('1'):
                return False, f"Значение матрицы для {y_id},{x_id} = {value} должно быть в интервале [0, 1]"
            row_values[x_id] = value

        matrix[y_id] = row_values

    return True, matrix


def read_input(filename: str) -> Tuple[
    bool, Union[Tuple[str, List[str], Dict[str, Decimal], List[str], Dict[str, Dict[str, Decimal]]], str]]:
    success, result = read_file_contents(filename)
    if not success:
        return False, result
    lines = result

    success, error = validate_basic_structure(lines)
    if not success:
        return False, error

    success, result = parse_premise(lines[0])
    if not success:
        return False, result
    premise = result

    success, result = parse_y_ids(lines[1])
    if not success:
        return False, result
    y_ids = result

    success, result = parse_t_values(lines[2], y_ids)
    if not success:
        return False, result
    t_values = result

    success, result = parse_x_ids(lines[3])
    if not success:
        return False, result
    x_ids = result

    success, result = parse_matrix(lines[4:], y_ids, x_ids)
    if not success:
        return False, result
    matrix = result

    return True, (premise, y_ids, t_values, x_ids, matrix)


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


def write_output(filename: str, output_str: str) -> Tuple[bool, Optional[str]]:
    file_obj = open(filename, 'w', encoding='utf-8')
    if file_obj is None:
        return False, f"Ошибка записи в файл {filename}"

    file_obj.write(output_str)
    file_obj.close()
    return True, None


def main():
    success, result = read_input('input.txt')
    if not success:
        print(f"Ошибка: {result}")
        return

    premise, y_ids, t_values, x_ids, matrix = result

    tnorm = FuzzyCompositionLukasiewicz()
    system = System(tnorm, matrix, t_values)
    solutions = system.solve()

    output_str = format_output(premise, solutions, x_ids)

    success, error = write_output('output.txt', output_str)
    if not success:
        print(f"Ошибка: {error}")
        return

    print("Результат успешно записан в output.txt")
    print(output_str)


if __name__ == "__main__":
    main()
