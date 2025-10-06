"""
Лабораторная работа 3 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Лексический анализатор, который токенизирует строку на основе полученного шаблона токенов.
27.09.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""

from typing import List, Tuple, Optional


def lex(characters: str, token_patterns: List[Tuple[str, Optional[str]]]) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that splits a string into tokens using specified patterns.

    Processes the input string character by character, skipping whitespace and
    matching tokens against predefined patterns. Continues until the entire
    input string has been processed.

    Args:
        characters (str): The input string to tokenize.
        token_patterns (List[Tuple[str, Optional[str]]]): List of patterns and tags
            where each tuple contains (pattern, tag). Pattern can be a literal string
            or special pattern identifier like '[NAME]' or '[NUM]'.

    Returns:
        List[Tuple[str, str]]: List of tokens where each token is a tuple of
            (lexeme, tag). The lexeme is the actual text matched, and the tag
            is the token classification.

    Raises:
        SyntaxError: If an unknown character is encountered that doesn't match
            any of the defined token patterns.
    """
    pos = 0
    tokens = []
    length = len(characters)

    while pos < length:
        # Skip whitespace characters
        if characters[pos].isspace():
            pos += 1
            continue

        # Attempt to match a token at current position
        token, new_pos = try_match_token(characters, pos, token_patterns)
        if token is not None:
            tokens.append(token)
            pos = new_pos
        else:
            raise SyntaxError(f'Illegal character "{characters[pos]}" at position {pos} in string: "{characters}"')

    return tokens


def try_match_token(characters: str, pos: int, token_patterns: List[Tuple[str, Optional[str]]]) -> Tuple[Optional[Tuple[str, str]], int]:
    """
    Try to match a token at the current position using all available patterns.

    Iterates through all token patterns in order and returns the first successful match.
    This allows for precedence handling where patterns are checked in the order provided.

    Args:
        characters (str): The input string to tokenize.
        pos (int): Current position in the string to start matching from.
        token_patterns (List[Tuple[str, Optional[str]]]): List of patterns and tags
            to attempt matching against.

    Returns:
        Tuple[Optional[Tuple[str, str]], int]: A tuple containing:
            - Optional token tuple (lexeme, tag) if match found, None otherwise
            - New position in the string after the match (or unchanged if no match)
    """
    for pat, tag in token_patterns:
        if pat is None:
            continue

        result = try_match_pattern(characters, pos, pat, tag)
        if result is not None:
            token, new_pos = result
            return token, new_pos

    return None, pos


def try_match_pattern(characters: str, pos: int, pattern: str, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Try to match a specific pattern at the current position.

    Routes to appropriate matching function based on pattern type:
    - Special patterns like [NAME], [NUM], [WS] use dedicated matchers
    - Literal strings use direct comparison

    Args:
        characters (str): The input string to tokenize.
        pos (int): Current position in the string to start matching from.
        pattern (str): The pattern to match against. Can be a literal string
            or special pattern identifier.
        tag (Optional[str]): The tag to assign to the token if matched.

    Returns:
        Optional[Tuple[Tuple[str, str], int]]: A tuple containing:
            - Token tuple (lexeme, tag) if match successful
            - New position in the string after the match
            Returns None if no match found.
    """
    if pattern == '[NAME]':
        return match_name(characters, pos, tag)
    elif pattern == '[NUM]':
        return match_num(characters, pos, tag)
    elif pattern == '[WS]':
        return None  # Whitespace already handled in main lex function
    else:
        return match_literal(characters, pos, pattern, tag)


def match_name(characters: str, pos: int, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a variable name pattern: [a-zA-Z][a-zA-Z0-9]*

    Variable names must start with a letter and can be followed by any
    combination of letters and digits.

    Args:
        characters (str): The input string to scan.
        pos (int): Current position in the string to start matching from.
        tag (Optional[str]): The tag to assign to the matched name token.

    Returns:
        Optional[Tuple[Tuple[str, str], int]]: A tuple containing:
            - Token tuple (name_string, tag) if a valid name is found
            - New position after the name
            Returns None if no valid name pattern is found at current position.
    """
    if not characters[pos].isalpha():
        return None

    start = pos
    pos += 1
    length = len(characters)

    # Continue matching alphanumeric characters
    while pos < length and characters[pos].isalnum():
        pos += 1

    token_text = characters[start:pos]
    return (token_text, tag), pos


def match_num(characters: str, pos: int, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a number pattern (integer or decimal).

    Supports two formats:
    1. Digits followed by optional decimal point and digits (e.g., "123", "45.67")
    2. Decimal point followed by digits (e.g., ".89")

    Args:
        characters (str): The input string to scan.
        pos (int): Current position in the string to start matching from.
        tag (Optional[str]): The tag to assign to the matched number token.

    Returns:
        Optional[Tuple[Tuple[str, str], int]]: A tuple containing:
            - Token tuple (number_string, tag) if a valid number is found
            - New position after the number
            Returns None if no valid number pattern is found at current position.
    """
    length = len(characters)

    # Case 1: Number starts with digit (integer or decimal)
    if characters[pos].isdigit():
        start = pos

        # Match integer part
        while pos < length and characters[pos].isdigit():
            pos += 1

        # Match decimal part if present
        if pos < length and characters[pos] == '.' and pos + 1 < length and characters[pos + 1].isdigit():
            pos += 1
            while pos < length and characters[pos].isdigit():
                pos += 1

        token_text = characters[start:pos]
        return (token_text, tag), pos

    # Case 2: Number starts with decimal point (fractional number)
    elif characters[pos] == '.' and pos + 1 < length and characters[pos + 1].isdigit():
        start = pos
        pos += 1
        while pos < length and characters[pos].isdigit():
            pos += 1

        token_text = characters[start:pos]
        return (token_text, tag), pos

    return None


def match_literal(characters: str, pos: int, pattern: str, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a literal pattern string at the current position.

    Performs exact string comparison to check if the pattern appears
    at the current position in the input string.

    Args:
        characters (str): The input string to scan.
        pos (int): Current position in the string to start matching from.
        pattern (str): The literal string pattern to match.
        tag (Optional[str]): The tag to assign to the matched token.

    Returns:
        Optional[Tuple[Tuple[str, str], int]]: A tuple containing:
            - Token tuple (pattern_string, tag) if pattern matches
            - New position after the pattern
            Returns None if pattern doesn't match at current position.
    """
    pattern_len = len(pattern)
    if characters.startswith(pattern, pos):
        if tag is not None:
            token = (pattern, tag)
            return token, pos + pattern_len
        else:
            return (pattern, ''), pos + pattern_len  # Return empty tag if tag is None but pattern matches
    return None