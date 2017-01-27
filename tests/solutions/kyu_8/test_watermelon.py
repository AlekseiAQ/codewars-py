"""Watermelon"""

import pytest

from solutions.kyu_8.watermelon import divide

EXAMPLES = (
    ('arg', 'expected'),
    [
        (4, True),
        (2, False),
        (5, False),
        (88, True),
        (100, True),
        (67, False),
        (90, True),
        (10, True),
        (99, False),
        (32, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert divide(arg) == expected
