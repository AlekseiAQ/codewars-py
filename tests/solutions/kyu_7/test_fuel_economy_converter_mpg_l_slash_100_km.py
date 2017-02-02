"""Fuel economy converter (mpg  <-> L/100 km)"""

import pytest

from solutions.kyu_7.fuel_economy_converter_mpg_l_slash_100_km import mpg2lp100km, lp100km2mpg

EXAMPLES_FOR_MPG = (
    ('arg', 'expected'),
    [
        (42, 5.6),
        (100, 2.35),
    ]
)


@pytest.mark.parametrize(*EXAMPLES_FOR_MPG)
def test_returns_correct_result_for_mpg(arg, expected):
    assert mpg2lp100km(arg) == expected


EXAMPLES_FOR_LP100K = (
    ('arg', 'expected'),
    [
        (9, 26.13),
        (100, 2.35),
    ]
)


@pytest.mark.parametrize(*EXAMPLES_FOR_LP100K)
def test_returns_correct_result_for_lp100k(arg, expected):
    assert lp100km2mpg(arg) == expected
