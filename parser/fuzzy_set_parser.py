from fuzzy_set import FuzzySet

from parser.fuzzy_set_lexer import fuzzy_set_lex

class FuzzySetParserFactory:
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
        result = self.expression()
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

    def expression(self):
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

            element = self.match('VAR')
            if not element:
                raise SyntaxError('Expected VAR token')
            if element in elements_of_set:
                raise SyntaxError(f'Element "{element}" is multiplicity defined')

            if not self.match('COMMA'):
                raise SyntaxError('Expected COMMA token')

            degree = self.match('NUM')
            if not degree:
                raise SyntaxError('Expected NUM token')
            degree = float(degree)
            if not 0 <= degree <= 1:
                raise SyntaxError(f'Degree of element "{element}" must be between 0 and 1')

            if not self.match('ETUPLE'):
                raise SyntaxError('Expected ETUPLE token')

            elements_of_set.append(element)
            degree_of_membership_of_set.append(degree)

            if not self.match('COMMA'):
                break

        if not self.match('EFSET'):
            raise SyntaxError('Expected EFSET token')

        return fuzzy_set_name, elements_of_set, degree_of_membership_of_set


class FuzzySetParser:
    def __init__(self, list_of_fuzzy_sets: list[FuzzySet]):
        self._fuzzy_sets = list_of_fuzzy_sets
        self._names = [i.name for i in list_of_fuzzy_sets]

    def parse(self, input_string):
        tokens = fuzzy_set_lex(input_string)
        parser = FuzzySetParserFactory(tokens)
        ast = parser.parse()

        if ast[0] in self._names:
            raise SyntaxError(f'Fuzzy set "{ast[0]}" is multiplicity defined')

        fuzzy_set = FuzzySet(*ast)

        self._fuzzy_sets.append(fuzzy_set)

        return fuzzy_set