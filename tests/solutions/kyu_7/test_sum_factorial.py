"""Sum Factorial"""

import pytest

from solutions.kyu_7.sum_factorial import sum_factorial

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([4, 6], 744),
        ([5, 4, 1], 145),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_factorial(arg) == expected
