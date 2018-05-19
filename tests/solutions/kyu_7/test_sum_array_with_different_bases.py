"""Sum Array with different bases"""

import pytest

from solutions.kyu_7.sum_array_with_different_bases import sum_it_up

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([["101", 2], ["10", 8]], 13),
        ([["ABC", 16], ["11", 2]], 2751),
        ([["101", 16], ["7640", 8], ["1", 9]], 4258),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_it_up(arg) == expected
