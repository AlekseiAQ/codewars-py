"""Calculate average """

import pytest

from solutions.kyu_8.calculate_average import find_average

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([ 1, 2, 3 ], 2),
        ([], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_average(arg) == expected
