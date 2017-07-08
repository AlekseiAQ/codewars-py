"""Validate Credit Card Number"""

import pytest

from solutions.kyu_6.validate_credit_card_number import validate

EXAMPLES = (
    ('arg', 'expected'),
    [
        (123, False),
        (1, False),
        (1230, True),
        (8675309, False),
        (4111111111111111, True),
        (2626262626262626, True),
        (922030, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate(arg) == expected
