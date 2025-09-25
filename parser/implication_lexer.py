from typing import List, Tuple
import parser.lexer as lexer

implication_token_patterns = [
    ('~>',     'FIMP'),
    ('[NAME]', 'NAME'),
    ('[WS]',    None),
]


def implication_lex(characters: str) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that tokenizes a string based on predefined token patterns.

    Args:
        characters (str): The input string to be tokenized.

    Returns:
        list of tuples: A list of tokens where each token is a tuple containing the matched text and its corresponding tag.
    """
    return lexer.lex(characters, implication_token_patterns)
