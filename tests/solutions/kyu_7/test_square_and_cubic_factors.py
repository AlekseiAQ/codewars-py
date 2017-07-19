"""Square and Cubic Factors"""

import pytest

from solutions.kyu_7.square_and_cubic_factors import factors

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, [[], []]),
        (4, [[2], []]),
        (16, [[2, 4], [2]]),
        (81, [[3, 9], [3]]),
        (80, [[2, 4], [2]]),
        (100, [[2, 5, 10], []]),
        (5, [[], []]),
        (120, [[2], [2]]),
        (18, [[3], []]),
        (8, [[2], [2]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert factors(arg) == expected
