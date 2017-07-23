"""Character Concatenation"""

import pytest

from solutions.kyu_7.character_concatenation import char_concat

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("abcdef", "af1be2cd3"),
        ("abc!def", "af1be2cd3"),
        ("abc def", "af1be2cd3"),
        ("CodeWars", "Cs1or2da3eW4"),
        ("CodeWars Rocks", "Cs1ok2dc3eo4WR5a 6rs7"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert char_concat(arg) == expected
