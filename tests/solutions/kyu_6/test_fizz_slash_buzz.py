"""Fizz / Buzz"""

import pytest

from solutions.kyu_6.fizz_slash_buzz import solution

EXAMPLES = (
    ('arg', 'expected'),
    [
        (20, [5,2,1]),
        (2, [0,0,0]),
        (30, [8,4,1]),
        (300, [80,40,19]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solution(arg) == expected
