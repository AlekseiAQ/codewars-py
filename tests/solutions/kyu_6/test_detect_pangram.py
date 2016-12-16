"""Detect Pangram"""

import pytest

from solutions.kyu_6.detect_pangram import is_pangram

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("The quick, brown fox jumps over the lazy dog!", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_pangram(arg) == expected
