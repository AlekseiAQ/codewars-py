"""Double Trouble"""

import pytest

from solutions.kyu_7.double_trouble import trouble

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 3, 5, 6, 7, 4, 3], 7), [1, 3, 5, 6, 7, 4]),
        (([4, 1, 1, 1, 4], 2), [4, 1, 4]),
        (([2, 2, 2, 2, 2, 2], 4), [2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert trouble(*args) == expected
