"""Duplicate Encoder"""

import pytest

from solutions.kyu_6.duplicate_encoder import duplicate_encode

EXAMPLES = (
    ('word', 'expected'),
    [
        ("din", "((("),
        ("recede", "()()()"),
        ("Success", ")())())"),
        ("(( @", "))(("),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(word, expected):
    assert duplicate_encode(word) == expected
