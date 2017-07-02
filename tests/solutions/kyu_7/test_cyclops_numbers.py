"""Cyclops numbers"""

import pytest

from solutions.kyu_7.cyclops_numbers import cyclops

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, False),
        (5, True),
        (3, False),
        (13, False),
        (27, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cyclops(arg) == expected
