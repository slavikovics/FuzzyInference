from fuzzy_set import FuzzySet
from fuzzy_implication import ImplicationScheme


class InferenceInput:
    def __init__(self):
        self.sets = []
        self.implications = []

    def __check_if_already_has_set(self, new_set_name):
        for fuzzy_set in self.sets:
            if new_set_name == fuzzy_set.name:
                return True

        return False

    def __check_if_already_has_implication(self, new_implication :ImplicationScheme):
        for fuzzy_implication in self.implications:
            if (new_implication.first == fuzzy_implication.first and
                    new_implication.second == fuzzy_implication.second):
                return True

        return False

    def check_ready_for_inference(self):
        pass

    def add_set(self, new_set :FuzzySet):
        if self.__check_if_already_has_set(new_set.name):
            raise AttributeError(f'Set with the name "{new_set.name}" has already been added.')

        self.sets.append(new_set)

    def add_implication(self, new_implication :ImplicationScheme):
        if self.__check_if_already_has_implication(new_implication):
            raise AttributeError(f'Implication "{new_implication}" has already been added.')

        if (not self.__check_if_already_has_set(new_implication.first) or not
            self.__check_if_already_has_set(new_implication.second)):
            raise AttributeError(f'All sets featured in implication must be added.')

        self.implications.append(new_implication)