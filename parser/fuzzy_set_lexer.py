from typing import List, Tuple
import parser.lexer as lexer
import os
import json


def load_tokens():
    file_path = os.path.join(os.path.dirname(__file__), 'set_token_patterns.json')
    with open(file_path, 'r', encoding='utf-8') as patterns:
        data = json.load(patterns)

    return list(data.items())


set_token_patterns = load_tokens()


def fuzzy_set_lex(characters: str) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that tokenizes a string based on predefined token patterns.

    Args:
        characters (str): The input string to be tokenized.

    Returns:
        list of tuples: A list of tokens where each token is a tuple containing the matched text and its corresponding tag.
    """
    return lexer.lex(characters, set_token_patterns)
