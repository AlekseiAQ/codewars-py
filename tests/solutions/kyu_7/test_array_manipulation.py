"""Array Manipulation"""

import pytest

from solutions.kyu_7.array_manipulation import array_manip

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28],
            [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]),
        ([ 2, 4, 18, 16, 7, 3, 9, 13, 18, 10 ],
            [3, 7, -1, 18, 9, 9, 10, 18, -1, -1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert array_manip(arg) == expected
