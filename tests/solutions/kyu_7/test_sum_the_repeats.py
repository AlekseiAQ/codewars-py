"""Sum the Repeats"""

import pytest

from solutions.kyu_7.sum_the_repeats import repeat_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([[1, 2, 3], [2, 8, 9], [7, 123, 8]], 10),
        ([[1], [2], [3, 4, 4, 4], [123456789]], 0),
        ([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]], 9),
        ([[1]], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert repeat_sum(arg) == expected
