"""Is every value in the array an array?"""

import pytest

from solutions.kyu_7.is_every_value_in_the_array_an_array import arr_check

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], True),
        ([['string']], True),
        ([[], {}], False),
        ([[1], [2], [3]], True),
        (["A", "R", "R", "A", "Y"], False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arr_check(arg) == expected
