"""Simple arithmetic progression"""

import pytest

from solutions.kyu_6.simple_arithmetic_progression import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4,5], 4),
        ([1,2,3,5,7,9], 5),
        ([0,5,8,9,11,13,14,16,17,19], 10),
        ([0,1,2,3,5,6,7,11,13,15,17,19], 17),
        ([0,1,4,5,7,9,10,13,15,16,18,19], 15),
        ([0,1,2,3,5,8,11,13,14,16,18,19], 13),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
