"""Regexp basics - parsing prices"""

import pytest

from solutions.kyu_7.regexp_basics_parsing_prices import to_cents

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", None),
        ("1", None),
        ("1.23", None),
        ("$1", None),
        ("$1.23", 123),
        ("$99.99", 9999),
        ("$12345678.90", 1234567890),
        ("$9.69", 969),
        ("$9.70", 970),
        ("$9.71", 971),
        ("$1.23\n", None),
        ("\n$1.23", None),
        ("$0.69", 69),
        ("$9.69$4.3.7", None),
        ("$9.692", None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert to_cents(arg) == expected
