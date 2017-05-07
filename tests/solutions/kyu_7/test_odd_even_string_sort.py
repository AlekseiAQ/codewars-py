"""Odd-Even String Sort"""

import pytest

from solutions.kyu_7.odd_even_string_sort import sort_my_string

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("CodeWars", "CdWr oeas"),
        ("YCOLUE'VREER", "YOU'RE CLEVER"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_my_string(arg) == expected
