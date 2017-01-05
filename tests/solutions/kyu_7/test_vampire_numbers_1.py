"""Vampire Numbers"""

import pytest

from solutions.kyu_7.vampire_numbers_1 import vampire_test

EXAMPLES = (
    ('args', 'expected'),
    [
        ((21,6), True),
        ((204,615), True),
        ((30,-51), True),
        ((-246,-510), False),
        ((210,600), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert vampire_test(*args) == expected
