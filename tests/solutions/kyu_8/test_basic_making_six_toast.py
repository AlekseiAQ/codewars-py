"""BASIC: Making Six Toast."""

import pytest

from solutions.kyu_8.basic_making_six_toast import six_toast

EXAMPLES = (
    ('arg', 'expected'),
    [
        (15, 9),
        (6, 0),
        (3, 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert six_toast(arg) == expected
