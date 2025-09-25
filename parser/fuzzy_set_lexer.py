from typing import List, Tuple
import parser.lexer as lexer

set_token_patterns = [
    ('{',      'SFSET'),
    ('}',      'EFSET'),
    ('<',      'STUPLE'),
    ('>',      'ETUPLE'),
    (',',      'COMMA'),
    ('=',      'EQUATE'),
    ('[NAME]', 'NAME'),
    ('[NUM]',  'NUM'),
    ('[VAR]',  'VAR'),
    ('[WS]',    None),
]


def fuzzy_set_lex(characters: str) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that tokenizes a string based on predefined token patterns.

    Args:
        characters (str): The input string to be tokenized.

    Returns:
        list of tuples: A list of tokens where each token is a tuple containing the matched text and its corresponding tag.
    """
    return lexer.lex(characters, set_token_patterns)
