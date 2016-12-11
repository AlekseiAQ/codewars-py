"""Triangular Treasure"""

import pytest

from solutions.kyu_7.triangular_treasure import triangular

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, 0),
        (2, 3),
        (3, 6),
        (-10, 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert triangular(arg) == expected