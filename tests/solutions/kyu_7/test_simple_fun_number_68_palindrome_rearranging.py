"""Simple Fun #68: Palindrome Rearranging"""

import pytest

from solutions.kyu_7.simple_fun_number_68_palindrome_rearranging import palindrome_rearranging

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("aabb",True),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc",False),
        ("abbcabb",True),
        ("zyyzzzzz",True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert palindrome_rearranging(arg) == expected
