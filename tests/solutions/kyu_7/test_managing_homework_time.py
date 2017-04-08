"""Managing Homework Time"""

import pytest

from solutions.kyu_7.managing_homework_time import time_per_day

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([(1, 20), (2, 10), (3, 15), (4, 10)], 0.31),
        ([(2, 25), (5, 10), (6, 15)], 0.47)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert time_per_day(arg) == expected
