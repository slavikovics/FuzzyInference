from fuzzy_set import FuzzySet
from fuzzy_implication import ImplicationScheme


class InferenceStep:
    def __init__(self, left_set, implication_scheme, result, equal_to = None):
        self.left_set = left_set
        self.implication_scheme = implication_scheme
        self.result = result
        self.equal_to = None
