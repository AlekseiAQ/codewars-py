"""Ordering  the words!"""

import pytest

from solutions.kyu_7.ordering_the_words import order_word

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hello, World!", " !,HWdellloor"),
        ("bobby", "bbboy"),
        ("", "Invalid String!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert order_word(arg) == expected
