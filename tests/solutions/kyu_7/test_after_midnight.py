"""After(?)  Midnight"""

import pytest

from solutions.kyu_7.after_midnight import day_and_time

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0,'Sunday 00:00'),
        (-3,'Saturday 23:57'),
        (45,'Sunday 00:45'),
        (759,'Sunday 12:39'),
        (1236,'Sunday 20:36'),
        (1447,'Monday 00:07'),
        (7832,'Friday 10:32'),
        (18876,'Saturday 02:36'),
        (259180,'Thursday 23:40'),
        (-349000,'Tuesday 15:20'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert day_and_time(arg) == expected
