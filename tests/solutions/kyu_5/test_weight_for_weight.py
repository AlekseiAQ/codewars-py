"""Weight for weight"""

import pytest

from solutions.kyu_5.weight_for_weight import order_weight

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("103 123 4444 99 2000",
            "2000 103 123 4444 99"),
        ("2000 10003 1234000 44444444 9999 11 11 22 123",
            "11 11 2000 10003 22 123 1234000 44444444 9999"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert order_weight(arg) == expected
