"""The Barksdale Code"""

import pytest

from solutions.kyu_7.the_barksdale_code import decode

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("4103432323", "6957678787"),
        ("4103438970", "6957672135"),
        ("4104305768", "6956750342"),
        ("4102204351", "6958856709"),
        ("4107056043", "6953504567"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert decode(arg) == expected
