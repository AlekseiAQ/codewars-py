"""Sum of numerous arguments"""

import pytest

from solutions.kyu_7.sum_of_numerous_arguments import find_sum

EXAMPLES = (
    ("args", "expected"),
    [
        ((1, 3, 5), 9),
        ((), 0),
        ((1, -2, 4), -1),
        ((0, ), 0),
        ((1, 1, 5), 7),
        ((1, 1, 1, 1, 1, 1, 1, 1, 0), 8),
        ((-1, -1, 5), -1),
        ((-1, -1, -5), -1),
        ((0, -1, 5), -1),
        ((0, 0, 0), 0),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert find_sum(*args) == expected
