"""Sorted? yes? no? how?"""

import pytest

from solutions.kyu_7.sorted_yes_no_how import is_sorted_and_how

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2], 'yes, ascending'),
        ([15, 7, 3, -8], 'yes, descending'),
        ([4, 2, 30], 'no'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_sorted_and_how(arg) == expected
