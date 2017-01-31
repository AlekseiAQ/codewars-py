"""Factorial Factory"""

import pytest

from solutions.kyu_7.factorial_factory import factorial

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 1),
        (5, 120),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert factorial(arg) == expected
