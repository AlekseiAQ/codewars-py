"""Transportation on vacation """

import pytest

from solutions.kyu_8.transportation_on_vacation import rental_car_cost

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 40),
        (4, 140),
        (7, 230),
        (8, 270),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert rental_car_cost(arg) == expected
