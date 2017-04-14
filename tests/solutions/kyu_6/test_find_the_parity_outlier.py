"""Find The Parity Outlier"""

import pytest

from solutions.kyu_6.find_the_parity_outlier import find_outlier

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([2, 6, 8, 10, 3], 3),
        ([2, 4, 0, 100, 4, 11, 2602, 36], 11),
        ([160, 3, 1719, 19, 11, 13, -21], 160),
        ([1, 2, 4, 6], 1),
        ([2, 1, 4, 6], 1),
        ([2, 4, 1, 6], 1),
        ([2, 4, 6, 1, 8], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_outlier(arg) == expected
