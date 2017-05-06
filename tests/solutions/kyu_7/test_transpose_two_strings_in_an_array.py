"""Transpose two strings in an array"""

import pytest

from solutions.kyu_7.transpose_two_strings_in_an_array import transpose_two_strings

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["Hello","World"], "H W\ne o\nl r\nl l\no d"),
        (["joey","louise"], "j l\no o\ne u\ny i\n  s\n  e"),
        (["a","cat"], "a c\n  a\n  t"),
        (["cat",""], "c  \na  \nt  "),
        (["!a!a!","?b?b"], "! ?\na b\n! ?\na b\n!  "),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert transpose_two_strings(arg) == expected
