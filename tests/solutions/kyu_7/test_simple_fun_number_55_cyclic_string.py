"""Simple Fun #55: Cyclic String"""

import pytest

from solutions.kyu_7.simple_fun_number_55_cyclic_string import cyclic_string

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("cabca", 3),
        ("aba", 2),
        ("ccccccccccc", 1),
        ("abaca", 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cyclic_string(arg) == expected
