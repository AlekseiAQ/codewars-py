"""Breaking chocolate problem"""

import pytest

from solutions.kyu_7.breaking_chocolate_problem import break_chocolate

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5, 5), 24),
        ((1, 1), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert break_chocolate(*args) == expected
