"""Discover The Original Price"""

import pytest

from solutions.kyu_7.discover_the_original_price import discover_original_price

EXAMPLES = (
    ('discounted_price', 'sale_percentage', 'expected'),
    [
        (75,25,100),
        (25,75,100),
        (75.75,25,101),
        (373.85,11.2,421),
        (458.2,17.13,552.91),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(discounted_price, sale_percentage, expected):
    assert discover_original_price(discounted_price, sale_percentage) == expected
