"""Find numbers which are divisible by given number"""

import pytest

from solutions.kyu_8.find_numbers_which_are_divisible_by_given_number import divisible_by

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1,2,3,4,5,6], 2), [2,4,6]),
        (([1,2,3,4,5,6], 3), [3,6]),
        (([0,1,2,3,4,5,6], 4), [0,4]),
        (([0], 4), [0]),
        (([1,3,5], 2), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert divisible_by(*args) == expected
