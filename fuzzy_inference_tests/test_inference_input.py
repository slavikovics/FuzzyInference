import unittest
from inference_engine import InferenceInput
from parser import parse_fuzzy_set, parse_fuzzy_implication


class InferenceInputTests(unittest.TestCase):

    def test_names_parsing(self):
        set_str_a = 'A = {<x1, 0.1>, <x2, 0.1>}'
        set_str_b = 'B = {<y1, 0.1>, <y2, 0.1>}'
        imp_str = 'A ~> B'
        fuzzy_set_a = parse_fuzzy_set(set_str_a)
        fuzzy_set_b = parse_fuzzy_set(set_str_b)

        fuzzy_implication = parse_fuzzy_implication(imp_str)

        inference_input = InferenceInput()
        inference_input.add_set(fuzzy_set_a)
        inference_input.add_set(fuzzy_set_b)
        inference_input.add_implication(fuzzy_implication)

        self.assertEqual(len(inference_input.implications), 1)
        self.assertEqual(len(inference_input.sets), 2)

    def test_add_duplicate_set(self):
        inference_input = InferenceInput()
        set_a = parse_fuzzy_set('A = {<x1, 0.1>, <x2, 0.1>}')
        set_a_dup = parse_fuzzy_set('A = {<x1, 0.1>, <x2, 0.1>}')

        inference_input.add_set(set_a)
        with self.assertRaises(AttributeError):
            inference_input.add_set(set_a_dup)

    def test_add_duplicate_implication(self):
        inference_input = InferenceInput()
        set_a = parse_fuzzy_set('A = {<x1, 0.1>, <x2, 0.1>}')
        set_b = parse_fuzzy_set('B = {<x1, 0.1>, <x2, 0.1>}')
        imp_ab = parse_fuzzy_implication('A ~> B')

        inference_input.add_set(set_a)
        inference_input.add_set(set_b)
        inference_input.add_implication(imp_ab)

        with self.assertRaises(AttributeError):
            inference_input.add_implication(imp_ab)

    def test_add_implication_with_missing_first_set(self):
        inference_input = InferenceInput()
        set_b = parse_fuzzy_set('B = {<x1, 0.1>, <x2, 0.1>}')
        imp_ab = parse_fuzzy_implication('A ~> B')

        inference_input.add_set(set_b)

        with self.assertRaises(AttributeError):
            inference_input.add_implication(imp_ab)

    def test_add_implication_with_missing_second_set(self):
        inference_input = InferenceInput()
        set_a = parse_fuzzy_set('A = {<x1, 0.1>, <x2, 0.1>}')
        imp_ab = parse_fuzzy_implication('A ~> B')

        inference_input.add_set(set_a)

        with self.assertRaises(AttributeError):
            inference_input.add_implication(imp_ab)

    def test_add_multiple_sets_and_implications(self):
        inference_input = InferenceInput()

        sets = [
            parse_fuzzy_set('A = {<x1, 0.1>, <x2, 0.1>}'),
            parse_fuzzy_set('B = {<x1, 0.1>, <x2, 0.1>}'),
            parse_fuzzy_set('C = {<x1, 0.1>, <x2, 0.1>}')
        ]

        implications = [
            parse_fuzzy_implication('A ~> B'),
            parse_fuzzy_implication('B ~> C'),
            parse_fuzzy_implication('A ~> C')
        ]

        for fuzzy_set in sets:
            inference_input.add_set(fuzzy_set)

        for implication in implications:
            inference_input.add_implication(implication)

        self.assertEqual(len(inference_input.sets), 3)
        self.assertEqual(len(inference_input.implications), 3)