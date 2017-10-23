"""Sum a list but ignore any duplicates"""

import pytest

from solutions.kyu_7.sum_a_list_but_ignore_any_duplicates import sum_no_duplicates

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 1, 2, 3], 5),
        ([1, 1, 2, 2, 3], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_no_duplicates(arg) == expected
