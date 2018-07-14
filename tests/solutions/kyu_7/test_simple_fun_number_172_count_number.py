"""Simple Fun #172: Count Number"""

import pytest

from solutions.kyu_7.simple_fun_number_172_count_number import count_number

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5, 5), 2),
        ((10, 5), 2),
        ((6, 12), 4),
        ((6, 169), 0),
        ((100000, 1000000000), 16),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert count_number(*args) == expected
