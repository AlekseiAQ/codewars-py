"""Boiled Eggs"""

import pytest

from solutions.kyu_7.boiled_eggs import cooking_time

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, 0),
        (5, 5),
        (10, 10),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cooking_time(arg) == expected
