"""Not all but sometimes all"""

import pytest

from solutions.kyu_7.not_all_but_sometimes_all import remove

EXAMPLES = (
    ('args', 'expected'),
    [
        (('this is a string',{'t':1, 'i':2}), 'hs s a string'),
        (('hello world',{'x':5, 'i':2}), 'hello world'),
        (('apples and bananas',{'a':50, 'n':1}), 'pples d bnns'),
        (('a',{'a':1, 'n':1}), ''),
        (('codewars',{'c':5, 'o':1, 'd':1, 'e':1, 'w':1, 'z':1, 'a':1, 'r':1, 's':1}), ''),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert remove(*args) == expected
