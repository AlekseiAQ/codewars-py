"""Count inversions"""

import pytest

from solutions.kyu_7.count_inversions import count_inversion

EXAMPLES = (
    ('arg', 'expected'),
    [
        ((1, 2, 3), 0),
        ((1, 3, 2), 1),
        ((3, 6, 2, 7, 3), 4),
        ((), 0),
        ((3, 3, 3), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert count_inversion(arg) == expected
