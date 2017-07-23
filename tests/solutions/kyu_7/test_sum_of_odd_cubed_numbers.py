"""Sum of Odd Cubed Numbers"""

import pytest

from solutions.kyu_7.sum_of_odd_cubed_numbers import cube_odd

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 3, 4], 28),
        ([-3, -2, 2, 3], 0),
        (["a", 12, 9, "z", 42], None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cube_odd(arg) == expected
