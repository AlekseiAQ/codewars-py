"""max diff - easy"""

import pytest

from solutions.kyu_7.max_diff_easy_1 import max_diff

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([0, 1, 2, 3, 4, 5, 6], 6),
        ([-0, 1, 2, -3, 4, 5, -6], 11),
        ([0, 1, 2, 3, 4, 5, 16], 16),
        ([16], 0),
        ([], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert max_diff(arg) == expected
