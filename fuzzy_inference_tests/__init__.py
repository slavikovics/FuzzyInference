"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Инициализация тестов
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_inference_tests.test_fuzzy_set_parser import FuzzySetParserTests
from fuzzy_inference_tests.test_implication_parser import FuzzyImplicationParserTests
from fuzzy_inference_tests.test_inference_input import InferenceInputTests
from fuzzy_inference_tests.test_godel_implication import TestGodelImplicationSolver
from fuzzy_inference_tests.test_weber_implication import TestWeberImplicationSolver
from fuzzy_inference_tests.test_min_tnorm import TestMinTNorm
from fuzzy_inference_tests.test_drastic_product import TestDrasticProduct
from fuzzy_inference_tests.test_fuzzy_set import TestFuzzySet