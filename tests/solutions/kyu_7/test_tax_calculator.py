"""Tax Calculator"""

import pytest

from solutions.kyu_7.tax_calculator import tax_calculator

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 0.1),
        (10, 1),
        (11, 1.07),
        (15, 1.35),
        (18, 1.56),
        (21, 1.75),
        (26, 2),
        (30, 2.2),
        (30.49, 2.21),
        (35, 2.35),
        (100, 4.3),
        (1000000, 30001.3),
        (0, 0),
        (-3, 0),
        (None, 0),
        ('monkey', 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert tax_calculator(arg) == expected
