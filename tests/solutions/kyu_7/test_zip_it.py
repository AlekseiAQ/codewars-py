"""Zip it!"""

import pytest

from solutions.kyu_7.zip_it import lstzip

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']

EXAMPLES = (
    ('args', 'expected'),
    [
        ((a, b, lambda a, b: str(a) + str(b)), ["1a", "2b", "3c", "4d", "5e"]),
        ((b, a, lambda a, b: str(a) + str(b)), ["a1", "b2", "c3", "d4", "e5"]),
        ((b, lstzip(a, b, lambda a, b: a * ord(b[0])), lambda a, b: str(a) + str(b)), ["a97", "b196", "c297", "d400", "e505"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert lstzip(*args) == expected
