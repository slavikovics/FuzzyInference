from typing import List, Tuple, Optional


def lex(characters: str, token_patterns: List[Tuple[str, Optional[str]]]) -> List[Tuple[str, str]]:
    """
    Lexical analyzer that splits a string into tokens using specified patterns.

    Args:
        characters (str): The input string to tokenize.
        token_patterns: List of patterns and tags (pattern, tag/None).

    Returns:
        List[Tuple[str, str]]: List of tokens (text, tag).

    Raises:
        SyntaxError: If an unknown character is encountered.
    """
    pos = 0
    tokens = []
    length = len(characters)

    while pos < length:
        if characters[pos].isspace():
            pos += 1
            continue

        token, new_pos = try_match_token(characters, pos, token_patterns)
        if token is not None:
            tokens.append(token)
            pos = new_pos
        else:
            raise SyntaxError(f'Illegal character "{characters[pos]}" at position {pos} in string: "{characters}"')

    return tokens


def try_match_token(characters: str, pos: int, token_patterns: List[Tuple[str, Optional[str]]]) -> Tuple[Optional[Tuple[str, str]], int]:
    """
    Try to match a token at the current position.

    Args:
        characters: The input string
        pos: Current position in the string
        token_patterns: List of patterns and tags

    Returns:
        Tuple of (token, new_position) or (None, pos) if no match found
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

    Args:
        characters: The input string
        pos: Current position in the string
        pattern: Pattern to match
        tag: Tag for the token

    Returns:
        Tuple of (token, new_position) or None if pattern doesn't match
    """
    if pattern == '[VAR]':
        return match_var(characters, pos, tag)
    elif pattern == '[NAME]':
        return match_name(characters, pos, tag)
    elif pattern == '[NUM]':
        return match_num(characters, pos, tag)
    elif pattern == '[WS]':
        return None  # Whitespace already handled in main function
    else:
        return match_literal(characters, pos, pattern, tag)


def match_var(characters: str, pos: int, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a variable pattern [a-zA-Z][a-zA-Z0-9]*
    """
    if not characters[pos].isalpha():
        return None

    start = pos
    pos += 1
    length = len(characters)

    while pos < length and characters[pos].isalnum():
        pos += 1

    token_text = characters[start:pos]
    return (token_text, tag), pos


def match_name(characters: str, pos: int, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a single uppercase letter name.
    """
    if characters[pos].isalpha() and characters[pos].isupper():
        token_text = characters[pos]
        return (token_text, tag), pos + 1
    return None


def match_num(characters: str, pos: int, tag: Optional[str]) -> Optional[Tuple[Tuple[str, str], int]]:
    """
    Match a number pattern (integer or decimal).
    """
    length = len(characters)

    # Case 1: Number starts with digit
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

    # Case 2: Number starts with decimal point
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
    Match a literal pattern string.
    """
    pattern_len = len(pattern)
    if characters.startswith(pattern, pos):
        if tag is not None:
            token = (pattern, tag)
            return token, pos + pattern_len
        else:
            return (pattern, ''), pos + pattern_len  # Return empty tag if tag is None but pattern matches
    return None