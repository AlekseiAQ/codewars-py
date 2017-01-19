"""Tip Calculator"""

import pytest

from solutions.kyu_8.tip_calculator import calculate_tip

EXAMPLES = (
    ('args', 'expected'),
    [
        ((30, "poor"), 2),
        ((20, "Excellent"), 4),
        ((20, "hi"), 'Rating not recognised'),
        ((107.65, "GReat"), 17),
        ((20, "great!"), 'Rating not recognised'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert calculate_tip(*args) == expected
