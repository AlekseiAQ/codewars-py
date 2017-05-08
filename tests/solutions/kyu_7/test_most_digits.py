"""Most digits"""

import pytest

from solutions.kyu_7.most_digits import find_longest

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 10, 100], 100),
        ([9000, 8, 800], 9000),
        ([8, 900, 500], 900),
        ([3, 40000, 100], 40000),
        ([1, 200, 100000], 100000),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_longest(arg) == expected
