"""Sum of a sequence"""

import pytest

from solutions.kyu_7.sum_of_a_sequence import sequence_sum

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, 6, 2), 12),
        ((1, 5, 1), 15),
        ((1, 5, 3), 5),
        ((0, 15, 3), 45),
        ((16, 15, 3), 0),
        ((2, 24, 22), 26),
        ((2, 2, 2), 2),
        ((2, 2, 1), 2),
        ((1, 15, 3), 35),
        ((15, 1, 3), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sequence_sum(*args) == expected
