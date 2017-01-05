"""Valid HK Phone Number"""

import pytest

from solutions.kyu_7.valid_hk_phone_number import is_valid_HK_phone_number, has_valid_HK_phone_number

EXAMPLES_ONE = (
    ('arg', 'expected'),
    [
        ("1234 5678", True),
        ("2359 1478", True),
        ("85748475", False),
        ("3857  4756", False),
        ("sklfjsdklfjsf", False),
        ("     1234 5678   ", False),
        ("abcd efgh", False),
        ("9684 2396", True),
        ("836g 2986", False),
        ("0000 0000", True),
        ("123456789", False),
        (" 987 634 ", False),
        ("    6    ", False),
        ("8A65 2986", False),
        ("8368 2aE6", False),
        ("8c65 2i86", False),
    ]
)

EXAMPLES_TWO = (
    ('arg', 'expected'),
    [
        ("Hello, my phone number is 1234 5678", True),
        ("I wonder if 2359 1478 is a valid phone number?", True),
        ("85748475 is definitely invalid", False),
        ("'3857  4756' is so close to a valid phone number!", False),
        ("sklfjsdklfjsf", False),
        ("     1234 5678   ", True),
        ("What about abcd efgh?", False),
        ("What about 9684 2396?", True),
        ("And 836g 2986?", False),
        ("skldfjsdklfjs0000 0000skldfjslkdfjs", True),
        ("123456789 is invalid", False),
        ("sdfssdfsdfdf 987 634 sdfsddsds", False),
        ("\n\n    6    \n\n", False),
        ("sdfsdsdfdf8A65 2986sdfsddfs", False),
        ("iwoeurwoeuwo8368 2aE6", False),
        ("8c65 2i86wioeruwioeruweoi", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES_ONE)
def test_returns_correct_result(arg, expected):
    assert is_valid_HK_phone_number(arg) == expected

@pytest.mark.parametrize(*EXAMPLES_TWO)
def test_returns_correct_result(arg, expected):
    assert has_valid_HK_phone_number(arg) == expected
