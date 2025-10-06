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


class TestInferenceEngine(unittest.TestCase):

    def test_simple_inference_1(self):
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

    def test_simple_inference_1_inverse(self):
        set1 = parse_fuzzy_set('A = {<x3, 1>, <x2, 0.2>, <x1, 0.3>}')
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

    def test_simple_inference_2(self):
        set1 = parse_fuzzy_set('A = {<x1, 0>, <x2, 1>, <x3, 0.5>}')
        set2 = parse_fuzzy_set('B = {<y1, 0>, <y2, 1>}')

        imp1 = parse_fuzzy_implication('A ~> B')

        inference_input = InferenceInput()
        inference_input.add_set(set1)
        inference_input.add_set(set2)
        inference_input.add_implication(imp1)

        pipeline = InferencePipeline(inference_input)
        pipeline.inference()

        steps = [
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.5>, <y2, 1>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_2_inverse(self):
        set1 = parse_fuzzy_set('A = {<x2, 1>, <x1, 0>, <x3, 0.5>}')
        set2 = parse_fuzzy_set('B = {<y2, 1>, <y1, 0>}')

        imp1 = parse_fuzzy_implication('A ~> B')

        inference_input = InferenceInput()
        inference_input.add_set(set1)
        inference_input.add_set(set2)
        inference_input.add_implication(imp1)

        pipeline = InferencePipeline(inference_input)
        pipeline.inference()

        steps = [
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.5>, <y2, 1>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_3(self):
        set1 = parse_fuzzy_set('A = {<x1, 0.8>, <x2, 0.4>}')
        set2 = parse_fuzzy_set('B = {<y1, 0.7>, <y2, 0.3>}')
        set3 = parse_fuzzy_set('C = {<z1, 0.9>, <z2, 0.1>}')

        imp1 = parse_fuzzy_implication('A ~> B')
        imp2 = parse_fuzzy_implication('B ~> C')

        inference_input = InferenceInput()
        inference_input.add_set(set1)
        inference_input.add_set(set2)
        inference_input.add_set(set3)
        inference_input.add_implication(imp1)
        inference_input.add_implication(imp2)

        pipeline = InferencePipeline(inference_input)
        pipeline.inference()

        steps = [
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.8>, <y2, 0.8>}')),
            InferenceStep(set2, imp2, parse_fuzzy_set('R = {<z1, 0.7>, <z2, 0.7>}')),
            InferenceStep(parse_fuzzy_set('R = {<y1, 0.8>, <y2, 0.8>}'), imp2,
                          parse_fuzzy_set('R = {<z1, 0.8>, <z2, 0.8>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_3_inverse(self):
        set1 = parse_fuzzy_set('A = {<x2, 0.4>, <x1, 0.8>}')
        set2 = parse_fuzzy_set('B = {<y2, 0.3>, <y1, 0.7>}')
        set3 = parse_fuzzy_set('C = {<z1, 0.9>, <z2, 0.1>}')

        imp1 = parse_fuzzy_implication('A ~> B')
        imp2 = parse_fuzzy_implication('B ~> C')

        inference_input = InferenceInput()
        inference_input.add_set(set1)
        inference_input.add_set(set2)
        inference_input.add_set(set3)
        inference_input.add_implication(imp1)
        inference_input.add_implication(imp2)

        pipeline = InferencePipeline(inference_input)
        pipeline.inference()

        steps = [
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.8>, <y2, 0.8>}')),
            InferenceStep(set2, imp2, parse_fuzzy_set('R = {<z1, 0.7>, <z2, 0.7>}')),
            InferenceStep(parse_fuzzy_set('R = {<y1, 0.8>, <y2, 0.8>}'), imp2,
                          parse_fuzzy_set('R = {<z1, 0.8>, <z2, 0.8>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_4(self):
        set1 = parse_fuzzy_set('A = {<x1, 0>, <x2, 0.5>}')
        set2 = parse_fuzzy_set('B = {<y1, 0.5>, <y2, 0.7>}')
        set3 = parse_fuzzy_set('C = {<x1, 0.5>, <x2, 1>}')

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
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.5>, <y2, 0.5>}')),
            InferenceStep(set3, imp1, parse_fuzzy_set('R = {<y1, 1>, <y2, 1>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(set3, imp2, parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp1,
                          parse_fuzzy_set('R = {<y1, 0.5>, <y2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}'), imp1, parse_fuzzy_set('R = {<y1, 1>, <y2, 1>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}'), imp2, parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}')),
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_4_inverse(self):
        set1 = parse_fuzzy_set('A = {<x1, 0>, <x2, 0.5>}')
        set2 = parse_fuzzy_set('B = {<y1, 0.5>, <y2, 0.7>}')
        set3 = parse_fuzzy_set('C = {<x2, 1>, <x1, 0.5>}')

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
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.5>, <y2, 0.5>}')),
            InferenceStep(set3, imp1, parse_fuzzy_set('R = {<y1, 1>, <y2, 1>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(set3, imp2, parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp1,
                          parse_fuzzy_set('R = {<y1, 0.5>, <y2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}'), imp1, parse_fuzzy_set('R = {<y1, 1>, <y2, 1>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}'), imp2, parse_fuzzy_set('R = {<x1, 1>, <x2, 1>}')),
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_5(self):
        set1 = parse_fuzzy_set('A = {<x1, 0.5>, <x2, 1>}')
        set2 = parse_fuzzy_set('B = {<x1, 0>, <x2, 0>}')
        set3 = parse_fuzzy_set('C = {<x1, 0.9>, <x2, 0.5>}')

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
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(set2, imp1, parse_fuzzy_set('R = {<x1, 0.0>, <x2, 0.0>}')),
            InferenceStep(set3, imp1, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.5>}')),
            InferenceStep(set2, imp2, parse_fuzzy_set('R = {<x1, 0.0>, <x2, 0.0>}')),
            InferenceStep(set3, imp2, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),

            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp1,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}'), imp1,
                          parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_5_inverse(self):
        set1 = parse_fuzzy_set('A = {<x2, 1>, <x1, 0.5>}')
        set2 = parse_fuzzy_set('B = {<x2, 0>, <x1, 0>}')
        set3 = parse_fuzzy_set('C = {<x1, 0.9>, <x2, 0.5>}')

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
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(set2, imp1, parse_fuzzy_set('R = {<x1, 0.0>, <x2, 0.0>}')),
            InferenceStep(set3, imp1, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.5>}')),
            InferenceStep(set2, imp2, parse_fuzzy_set('R = {<x1, 0.0>, <x2, 0.0>}')),
            InferenceStep(set3, imp2, parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),

            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}'), imp2,
                          parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}'), imp1,
                          parse_fuzzy_set('R = {<x1, 0.5>, <x2, 0.5>}')),
            InferenceStep(parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}'), imp1,
                          parse_fuzzy_set('R = {<x1, 0.9>, <x2, 0.9>}')),
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))
        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))

    def test_simple_inference_6_inverse(self):
        set1 = parse_fuzzy_set('A = {<x1, 0.5>, <x2, 1>}')
        set2 = parse_fuzzy_set('B = {<y2, 1>, <y1, 0.5>}')
        set3 = parse_fuzzy_set('C = {<z2, 1>, <z1, 0.5>}')

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
            InferenceStep(set1, imp1, parse_fuzzy_set('R = {<y1, 0.5>, <y2, 1.0>}')),
            InferenceStep(set1, imp2, parse_fuzzy_set('R = {<z1, 0.5>, <z2, 1.0>}'))
        ]

        self.assertEqual(len(pipeline.inference_steps), len(steps))

        for step in steps:
            self.assertTrue(pipeline.inference_steps.__contains__(step))
