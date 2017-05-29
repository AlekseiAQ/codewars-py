"""Loose Change!"""

import pytest

from solutions.kyu_7.loose_change_1 import change_count

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('dime penny dollar', '$1.11'),
        ('dime penny nickel', '$0.16'),
        ('quarter quarter', '$0.50'),
        ('dollar penny dollar', '$2.01'),
        ('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny', '$10.01'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert change_count(arg) == expected
