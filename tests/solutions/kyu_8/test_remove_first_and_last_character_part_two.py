"""Remove First and Last Character Part Two"""

import pytest

from solutions.kyu_8.remove_first_and_last_character_part_two import array

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('', None),
        ('1', None),
        ('1, 3', None),
        ('1,2,3', '2'),
        ('1,2,3,4', '2 3'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert array(arg) == expected
