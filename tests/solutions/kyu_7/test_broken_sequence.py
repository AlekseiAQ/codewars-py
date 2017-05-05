"""Broken sequence"""

import pytest

from solutions.kyu_7.broken_sequence import find_missing_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1 2 3 5", 4),
        ("1 5", 2),
        ("", 0),
        ("1 2 3 4 5", 0),
        ("2 3 4 5", 1),
        ("2 6 4 5 3", 1),
        ("2 1 4 3 a", 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_missing_number(arg) == expected
