"""Sum of Multiples"""

import pytest

from solutions.kyu_8.sum_of_multiples import sum_mul

EXAMPLES = (
    ('n', 'm', 'expected'),
    [
        (0, 0, 'INVALID'),
        (2, 9, 20),
        (4, -7, 'INVALID'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(n, m, expected):
    assert sum_mul(n, m) == expected
