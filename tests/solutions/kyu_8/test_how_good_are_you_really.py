"""How good are you really?"""

import pytest

from solutions.kyu_8.how_good_are_you_really import better_than_average

EXAMPLES = (
    ('args', 'expected'),
    [
        (([2, 3], 5), True),
        (([100, 40, 34, 57, 29, 72, 57, 88], 75), True),
        (([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert better_than_average(*args) == expected
