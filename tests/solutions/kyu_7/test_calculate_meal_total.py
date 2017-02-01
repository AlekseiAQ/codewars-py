"""Calculate Meal Total"""

import pytest

from solutions.kyu_7.calculate_meal_total import calculate_total

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5.00, 5, 10), 5.75),
        ((36.97, 7, 15), 45.10),
        ((0.00, 6, 18), 0.00),
        ((80.94, 0, 20), 97.13),
        ((54.96, 8, 0), 59.36),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert calculate_total(*args) == expected
