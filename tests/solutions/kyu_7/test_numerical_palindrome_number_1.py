"""Numerical Palindrome #1"""

import pytest

from solutions.kyu_7.numerical_palindrome_number_1 import palindrome

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1221,True),
        (123322,False),
        ("ACCDDCCA","Not valid"),
        ("1221","Not valid"),
        (-450,"Not valid"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert palindrome(arg) == expected
