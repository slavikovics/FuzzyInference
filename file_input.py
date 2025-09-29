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

from fuzzy_implication import ImplicationScheme
from parser import parse_fuzzy_set, parse_fuzzy_implication
from inference_engine import InferenceInput, InferenceStep, InferencePipeline

import os


def get_file(inference_input: InferenceInput):
    # file_name = input('Введите имя файла: ')
    file_name = 'input'

    print()

    if not file_name:
        print('Ошибка: Путь к файлу не может быть пустым')
        return

    if not os.path.exists(file_name):
        print(f'Ошибка: Файл "{file_name}" не существует')
        return

    if not os.path.isfile(file_name):
        print(f'Ошибка: "{file_name}" не является файлом')
        return

    with open(file_name, 'r') as f:
        input_fuzzy_sets(inference_input, f)
        input_fuzzy_implications(inference_input, f)


def input_fuzzy_sets(inference_input: InferenceInput, f):
    while True:
        fuzzy_set_str = f.readline().strip()

        if not fuzzy_set_str:
            return

        try:
            fuzzy_set = parse_fuzzy_set(fuzzy_set_str)
            inference_input.add_set(fuzzy_set)
        except Exception as e:
            print(f'Произошла ошибка: {e.args}.')


def input_fuzzy_implications(inference_input: InferenceInput, f):
    while True:
        fuzzy_implication_str = f.readline().strip()

        if not fuzzy_implication_str:
            return

        try:
            fuzzy_implication = parse_fuzzy_implication(fuzzy_implication_str)
            inference_input.add_implication(fuzzy_implication)
        except Exception as e:
            print(f'Произошла ошибка: {e.args}.')


def print_implications(schemes: list[ImplicationScheme]):
    for scheme in schemes:
        print(scheme.str_with_solution())
        print('')


def print_inference(inference_steps: list[InferenceStep]):
    for i, step in enumerate(inference_steps):
        print(f'{i + 1}. {str(step)}')


def main():
    inference_input = InferenceInput()
    get_file(inference_input)
    pipeline = InferencePipeline(inference_input)
    pipeline.inference()
    print_implications(inference_input.implications)
    print_inference(pipeline.inference_steps)


if __name__ == '__main__':
    main()
