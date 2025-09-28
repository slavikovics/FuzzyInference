from abc import ABC, abstractmethod
from fuzzy_set import FuzzySet


class AbstractFuzzyImplicationSolver(ABC):

    @abstractmethod
    def solve(self, left_set :FuzzySet, right_set :FuzzySet) -> list[list[float]]:
        pass