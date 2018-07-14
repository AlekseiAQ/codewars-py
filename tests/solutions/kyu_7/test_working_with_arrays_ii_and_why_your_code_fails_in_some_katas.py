"""Working with arrays II (and why your code fails in some katas)"""

import pytest

from solutions.kyu_7.working_with_arrays_ii_and_why_your_code_fails_in_some_katas import \
    remove_nth_element

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 2, 3, 4, 5], 4), [1, 2, 3, 4]),
        (([9, 7, 6, 9], 0), [7, 6, 9]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert remove_nth_element(*args) == expected
