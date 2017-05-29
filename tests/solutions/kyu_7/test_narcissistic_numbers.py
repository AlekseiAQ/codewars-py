"""Narcissistic Numbers """

import pytest

from solutions.kyu_7.narcissistic_numbers import is_narcissistic

EXAMPLES = (
    ('arg', 'expected'),
    [
        (153, True),
        (201, False),
        (259, False),
        (371, True),
        (407, True),
        (595, False),
        (825, False),
        (1634, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_narcissistic(arg) == expected
