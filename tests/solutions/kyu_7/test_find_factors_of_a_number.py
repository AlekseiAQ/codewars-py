"""Find factors of a number"""

import pytest

from solutions.kyu_7.find_factors_of_a_number import factors

EXAMPLES = (
    ('arg', 'expected'),
    [
        (-4, -1),
        (0, -1),
        (-12, -1),
        ('a', -1),
        (4.5, -1),
        ('hello world', -1),
        (54, [54,27,18,9,6,3,2,1]),
        (49, [49, 7, 1]),
        (1, [1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert factors(arg) == expected
