"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Тест нечёткого вывода
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

import unittest
from parser import parse_fuzzy_set, parse_fuzzy_implication
from inference_engine import InferenceInput, InferencePipeline, InferenceStep


class TestInference1(unittest.TestCase):

    def test_simple_inference(self):
        set1 = parse_fuzzy_set('A = {<x1, 0.3>, <x2, 0.2>, <x3, 1>}')
        set2 = parse_fuzzy_set('B = {<y1, 0.9>, <y2,  0.6>}')
        set3 = parse_fuzzy_set('C = {<y1, 1>, <y2, 1>}')

        imp1 = parse_fuzzy_implication('A ~> B')
        imp2 = parse_fuzzy_implication('A ~> C')

        inference_input = InferenceInput()
        inference_input.add_set(set1)
        inference_input.add_set(set2)
        inference_input.add_set(set3)
        inference_input.add_implication(imp1)
        inference_input.add_implication(imp2)

        pipeline = InferencePipeline(inference_input)
        pipeline.inference()

        steps = [
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.9>, <y2, 0.6>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<y1, 1.0>, <y2, 1.0>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))

        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))