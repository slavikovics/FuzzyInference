"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Парсер нечетких множеств
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_set import FuzzySet
from parser.fuzzy_set_lexer import fuzzy_set_lex


class FuzzySetParser:
    def __init__(self, tokens: list[tuple[str, str]]) -> None:
        """
        Initializes the Parser instance.

        Args:
            tokens (list[tuple[str, str]]): The list of tokens to parse.
        """
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        """
        Parses the entire token list into an abstract syntax tree (AST).
        Ensures that all tokens are consumed after a successful parse.

        Returns:
            Expr: The root of the parsed AST.

        Raises:
            SyntaxError: If the formula is syntactically incorrect, or if unconsumed tokens remain.
        """
        result = self.check_syntax()
        if self.pos < len(self.tokens):
            raise SyntaxError(f'Unexpected token at the end of the formula: {self.tokens[self.pos][0]}')
        return result

    def match(self, expected_tag: str):
        """
        Attempts to match the current token's tag with the `expected_tag`.
        If a match is found, the parser's position is advanced (`self.pos` is incremented).

        Args:
            expected_tag (str): The tag of the token expected (e.g., 'LPAREN', 'VAR').

        Returns:
            Optional[str]: The matched token's lexeme (value, e.g., '(' or 'A'),
                           or `None` if no match is found.
        """
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == expected_tag:
            self.pos += 1
            return self.tokens[self.pos - 1][0]
        return None

    def check_syntax(self):
        """
        Checks and validates the syntax of fuzzy set definition.

        Parses the fuzzy set structure including:
        - Set name and assignment operator
        - Set elements with their membership degrees
        - Validation of duplicate elements and degree ranges

        Returns:
            tuple: A tuple containing (fuzzy_set_name, elements_list, degrees_list)

        Raises:
            SyntaxError: If the syntax does not conform to expected fuzzy set notation
            ValueError: If membership degrees are outside the valid [0, 1] range
        """
        elements_of_set = []
        degree_of_membership_of_set = []

        fuzzy_set_name = self.match('NAME')
        if not fuzzy_set_name:
            raise SyntaxError('Expected NAME token')

        if not self.match('EQUATE'):
            raise SyntaxError('Expected EQUATE token')

        if not self.match('SFSET'):
            raise SyntaxError('Expected SFSET token')

        while self.match('STUPLE'):

            element = self.match('NAME')
            if not element:
                raise SyntaxError('Expected NAME token')
            if element in elements_of_set:
                raise SyntaxError(f'Element "{element}" is multiplicity defined')

            if not self.match('COMMA'):
                raise SyntaxError('Expected COMMA token')

            degree = self.match('NUM')
            if not degree:
                raise SyntaxError('Expected NUM token')
            degree = float(degree)
            if not 0 <= degree <= 1:
                raise ValueError(f'Degree of element "{element}" must be between 0 and 1')

            if not self.match('ETUPLE'):
                raise SyntaxError('Expected ETUPLE token')

            elements_of_set.append(element)
            degree_of_membership_of_set.append(degree)

            if self.match('EFSET'):
                return fuzzy_set_name, elements_of_set, degree_of_membership_of_set

            if not self.match('COMMA'):
                break

            if not self.match('STUPLE'):
                raise SyntaxError('Expected STUPLE token')
            self.pos -= 1

        if self.match('EFSET'):
            return fuzzy_set_name, elements_of_set, degree_of_membership_of_set

        raise SyntaxError('Expected EFSET token')


def parse_fuzzy_set(input_string):
    """
    Parses a fuzzy set definition string into a FuzzySet object.

    This is the main entry point for parsing fuzzy set notation. It coordinates
    the lexing and parsing process to transform a string representation into
    a structured FuzzySet object.

    Args:
        input_string (str): The fuzzy set definition string to parse.
                           Example: "A = {<a, 0.5>, <b, 0.8>}"

    Returns:
        FuzzySet: The parsed fuzzy set object.

    Raises:
        SyntaxError: If the input string contains syntax errors.
        ValueError: If membership degrees are invalid.
    """
    tokens = fuzzy_set_lex(input_string)
    parser = FuzzySetParser(tokens)
    ast = parser.parse()

    return FuzzySet(*ast)
