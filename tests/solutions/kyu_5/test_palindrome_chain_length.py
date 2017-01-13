"""Palindrome chain length"""

import pytest

from solutions.kyu_5.palindrome_chain_length import palindrome_chain_length

EXAMPLES = (
    ('arg', 'expected'),
    [
        (87, 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert palindrome_chain_length(arg) == expected
