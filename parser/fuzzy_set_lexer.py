"""
Лабораторная работа 3 по дисциплине ЛОИС

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

from typing import List, Tuple
import parser.lexer as lexer
import os
import json


def load_tokens():
    file_path = os.path.join(os.path.dirname(__file__), 'set_token_patterns.json')
    with open(file_path, 'r', encoding='utf-8') as patterns:
        data = json.load(patterns)

    return list(data.items())


def fuzzy_set_lex(characters: str) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that tokenizes a string based on predefined token patterns.

    Args:
        characters (str): The input string to be tokenized.

    Returns:
        list of tuples: A list of tokens where each token is a tuple containing the matched text and its corresponding tag.
    """
    set_token_patterns = load_tokens()
    return lexer.lex(characters, set_token_patterns)