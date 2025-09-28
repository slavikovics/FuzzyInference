from parser import parse_fuzzy_set, parse_fuzzy_implication
from inference_engine import InferenceInput, InferenceStep, InferencePipeline


def input_fuzzy_sets(inference_input :InferenceInput):
    while True:
        print('Введите нечёткое множество. Пример: "A = {<x1, 0.0>, <x2, 0.5>}". Для завершения ввода: "e".')
        fuzzy_set_str = input()

        if fuzzy_set_str == 'e':
            return

        try:
            fuzzy_set = parse_fuzzy_set(fuzzy_set_str)
            inference_input.add_set(fuzzy_set)
        except Exception as e:
            print(f'Произошла ошибка: {e.args}.')

        print('')


def input_fuzzy_implications(inference_input :InferenceInput):
    while True:
        print('Введите нечёткую импликацию. Пример: "A ~> B". Для завершения ввода: "e".')
        fuzzy_implication_str = input()

        if fuzzy_implication_str == 'e':
            return

        try:
            fuzzy_implication = parse_fuzzy_implication(fuzzy_implication_str)
            inference_input.add_implication(fuzzy_implication)
        except Exception as e:
            print(f'Произошла ошибка: {e.args}.')

        print('')


def print_inference(inference_steps :list[InferenceStep]):
    for i, step in enumerate(inference_steps):
        print(f'{i + 1}. {str(step)}')


def main():
    inference_input = InferenceInput()
    input_fuzzy_sets(inference_input)
    input_fuzzy_implications(inference_input)
    pipeline = InferencePipeline(inference_input)
    pipeline.inference()
    print_inference(pipeline.inference_steps)


if __name__ == '__main__':
    main()