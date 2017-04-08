"""How much will you spend?"""

import pytest

from solutions.kyu_7.how_much_will_you_spend import get_total

costs = {'socks':5, 'shoes':60, 'sweater':30}

EXAMPLES = (
    ('costs', 'items', 'tax', 'expected'),
    [
        (costs, ['socks', 'shoes'], 0.09, 70.85)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(costs, items, tax, expected):
    assert get_total(costs, items, tax) == expected
