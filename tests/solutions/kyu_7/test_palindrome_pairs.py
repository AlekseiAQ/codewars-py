"""Palindrome Pairs"""

import pytest

from solutions.kyu_7.palindrome_pairs import palindrome_pairs

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["dog", "cow", "tap", "god", "pat"], [[0, 3], [2, 4], [3, 0], [4, 2]]),
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [2, 4], [3, 2]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert palindrome_pairs(arg) == expected
