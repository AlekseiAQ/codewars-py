"""The mean of two means"""

import pytest

from solutions.kyu_7.the_mean_of_two_means import get_mean

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 3, 2, 4], 2, 3), 2.5),
        (([1, 3, 2], 2, 2), 2.25),
        (([1, 3, 2, 4], 1, 2), -1),
        (([1, 3, 2, 4], 2, 8), -1),
        (([1, -1, 2, -1], 2, 3), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert get_mean(*args) == expected
