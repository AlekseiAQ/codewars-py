"""Make a function that does arithmetic!"""

import pytest

from solutions.kyu_7.make_a_function_that_does_arithmetic import arithmetic

EXAMPLES = (
    ('a', 'b', 'operator', 'expected'),
    [
        (1, 2, "add", 3),
        (8, 2, "subtract", 6),
        (5, 2, "multiply", 10),
        (8, 2, "divide", 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, operator, expected):
    assert arithmetic(a, b, operator) == expected
