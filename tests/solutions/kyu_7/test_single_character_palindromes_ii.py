"""Single character palindromes II"""

import pytest

from solutions.kyu_7.single_character_palindromes_ii import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("abba", False),
        ("abbaa", True),
        ("abbx", True),
        ("aa", False),
        ("ab", True),
        ("abcba", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
