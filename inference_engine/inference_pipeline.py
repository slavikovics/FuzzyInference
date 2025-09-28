from typing import Optional
from inference_engine import InferenceInput
from fuzzy_set import FuzzySet
from fuzzy_implication import ImplicationScheme, GodelImplicationSolver
from fuzzy_conjunction import FuzzyConjunction
from inference_engine import InferenceStep


class InferencePipeline:

    def __init__(self, inference_input :InferenceInput):
        self.inference_input = inference_input
        self.tnorm = FuzzyConjunction.min
        self.implication_solver = GodelImplicationSolver()
        self.inference_steps = []

    def find_set_with_name(self, name :str) -> Optional[FuzzySet]:
        for fuzzy_set in self.inference_input.sets:
            if name == fuzzy_set.name:
                return fuzzy_set

        return None

    def calculate_implications(self):
        for implication in self.inference_input.implications:
            first = self.find_set_with_name(implication.first)
            second = self.find_set_with_name(implication.second)

            if first is None or second is None:
                implication.solution = None

            else:
                implication.solution = self.implication_solver.solve(first, second)

    def find_compatible_sets(self, implication_scheme :ImplicationScheme):
        first_set = self.find_set_with_name(implication_scheme.first)
        if first_set is None:
            return []

        result = []
        for fuzzy_set in self.inference_input.sets:
            if first_set.is_like(fuzzy_set):
                result.append(fuzzy_set)

        return result

    def apply_modus_ponens(self, fuzzy_set :FuzzySet, implication_scheme :ImplicationScheme, new_set_name :str) -> Optional[FuzzySet]:
        if implication_scheme.solution is None:
            return None

        conjunction = self.tnorm(fuzzy_set, implication_scheme.solution)
        if not conjunction:
            return None

        transposed = list(zip(*conjunction))
        sup = [max(col) for col in transposed]

        target_set = self.find_set_with_name(implication_scheme.second)
        if target_set is None:
            return None

        return FuzzySet(new_set_name, target_set.elements, sup)

    def check_for_duplicates(self, set_to_check :FuzzySet):
        if set_to_check is None:
            return None

        for fuzzy_set in self.inference_input.sets:
            if fuzzy_set == set_to_check:
                return fuzzy_set
        return None

    def inference(self):
        step_index = 1
        self.calculate_implications()
        changed = True

        while changed:
            changed = False

            for scheme in self.inference_input.implications:
                if scheme.solution is None:
                    continue

                for fuzzy_set in self.find_compatible_sets(scheme):
                    if fuzzy_set not in scheme.applied_sets:
                        result = self.apply_modus_ponens(fuzzy_set, scheme, f'_{step_index}')
                        scheme.applied_sets.append(fuzzy_set)

                        if result is None:
                            self.inference_steps.append(InferenceStep(fuzzy_set, scheme, None, None))
                            continue

                        duplicate = self.check_for_duplicates(result)
                        if duplicate is None:
                            self.inference_input.sets.append(result)

                        self.inference_steps.append(InferenceStep(fuzzy_set, scheme, result, duplicate))

                        changed = True
                        step_index += 1