"""Disagreeable ascii"""

import pytest

from solutions.kyu_7.disagreeable_ascii import get_weight

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Joe',254),
        ('CJ',205),
        ('cj',141),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_weight(arg) == expected
