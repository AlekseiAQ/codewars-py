"""Your order,  please"""

import pytest

from solutions.kyu_6.your_order_please import order

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert order(arg) == expected
