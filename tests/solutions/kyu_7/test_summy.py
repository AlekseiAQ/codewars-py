"""Summy"""

import pytest

from solutions.kyu_7.summy import summy

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1 2 3", 6),
        ("1 2 3 4", 10),
        ("1 2 3 4 5", 15),
        ("10 10", 20),
        ("0 0", 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert summy(arg) == expected
