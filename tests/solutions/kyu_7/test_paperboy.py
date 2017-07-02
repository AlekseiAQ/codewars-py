"""Paperboy"""

import pytest

from solutions.kyu_7.paperboy import cheapest_quote

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 0.10),
        (5, 0.49),
        (10, 0.97),
        (20, 1.93),
        (40, 3.85),
        (41, 3.95),
        (80, 7.70),
        (26, 2.52),
        (0, 0.0),
        (499, 48.06),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cheapest_quote(arg) == expected
