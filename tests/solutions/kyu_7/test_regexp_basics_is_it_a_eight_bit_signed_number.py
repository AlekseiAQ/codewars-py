"""Regexp Basics - is it a eight bit signed number?"""

import pytest

from solutions.kyu_7.regexp_basics_is_it_a_eight_bit_signed_number import signed_eight_bit_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", False),
        ("0", True),
        ("00", False),
        ("-0", False),
        ("55", True),
        ("-23", True),
        ("042", False),
        ("127", True),
        ("128", False),
        ("999", False),
        ("-128", True),
        ("-129", False),
        ("-999", False),
        ("1\n", False),
        ("1 ", False),
        (" 1", False),
        ("1\n2", False),
        ("+1", False),
        ("--1", False),
        ("1\n", False),
        ("1 ", False),
        (" 1", False),
        ("1\n2", False),
        ("+1", False),
        ("--1", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert signed_eight_bit_number(arg) == expected
