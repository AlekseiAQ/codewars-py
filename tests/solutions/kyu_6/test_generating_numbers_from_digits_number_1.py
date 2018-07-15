"""Generating Numbers  From Digits #1"""

import pytest

from solutions.kyu_6.generating_numbers_from_digits_number_1 import proc_arr

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['1', '2', '2', '3', '2', '3'],
            [60, 122233, 332221]),
        (['1', '2', '3', '0', '5', '1', '1', '3'],
            [3360, 1112335, 53321110]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert proc_arr(arg) == expected
