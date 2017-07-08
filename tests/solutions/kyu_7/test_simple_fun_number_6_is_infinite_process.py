"""Simple Fun #6: Is Infinite Process?"""

import pytest

from solutions.kyu_7.simple_fun_number_6_is_infinite_process import is_infinite_process

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, 6), False),
        ((2, 3), True),
        ((2, 10), False),
        ((0, 1), True),
        ((3, 1), True),
        ((10, 10), False),
        ((5, 10), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert is_infinite_process(*args) == expected
