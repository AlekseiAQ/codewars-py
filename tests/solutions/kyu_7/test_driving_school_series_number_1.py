"""Driving School Series #1 """

import pytest

from solutions.kyu_7.driving_school_series_number_1 import passed

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([10,10,10,18,20,20], 12),
        ([21,22,24], 'No pass scores registered.'),
        ([3,22,9,13,20,18,2,14,20,8,23,12,7,21,21,19,20,11,18,7,13,22,11,20,9], 10),
        ([19,16,8,11,25,10,29,22,23] ,11),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert passed(arg) == expected
