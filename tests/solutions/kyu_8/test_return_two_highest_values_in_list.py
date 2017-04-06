"""Return Two Highest Values in List"""

import pytest

from solutions.kyu_8.return_two_highest_values_in_list import two_highest

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([15, 20, 20, 17], [20, 17]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert two_highest(arg) == expected
