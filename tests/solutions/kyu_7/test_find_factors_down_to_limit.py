"""Find Factors Down to Limit"""

import pytest

from solutions.kyu_7.find_factors_down_to_limit import factors

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5, 1), [1, 5]),
        ((30, 2), [2, 3, 5, 6, 10, 15, 30]),
        ((100, 75), [100]),
        ((40, 5), [5, 8, 10, 20, 40]),
        ((1, 5), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert factors(*args) == expected
