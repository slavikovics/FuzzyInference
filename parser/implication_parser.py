"""
Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Главное меню программы
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from fuzzy_implication import ImplicationScheme
from parser.implication_lexer import implication_lex


class ImplicationParser:
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
        first = self.match('NAME')
        if first is None:
            raise SyntaxError(f'Unexpected token')

        if not self.match('FIMP'):
            raise SyntaxError(f'Unexpected token')

        second = self.match('NAME')
        if second is None:
            raise SyntaxError(f'Unexpected token')

        return first, second


def parse_fuzzy_implication(input_string):
    tokens = implication_lex(input_string)
    parser = ImplicationParser(tokens)
    ast = parser.parse()

    return ImplicationScheme(*ast)
